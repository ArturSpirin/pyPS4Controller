import struct


class Actions:
    """
    Actions are inherited in the Controller class.
    In order to bind to the controller events, subclass the Controller class and
    override desired action events in this class.
    """
    def __init__(self):
        pass

    def on_x_press(self):
        pass

    def on_x_release(self):
        pass

    def on_triangle_press(self):
        pass

    def on_triangle_release(self):
        pass

    def on_circle_press(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    def on_L1_press(self):
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        pass

    def on_L2_release(self):
        pass

    def on_R1_press(self):
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        pass

    def on_R2_release(self):
        pass

    def on_up_arrow_press(self):
        pass

    def on_up_down_arrow_release(self):
        pass

    def on_down_arrow_press(self):
        pass

    def on_left_arrow_press(self):
        pass

    def on_left_right_arrow_release(self):
        pass

    def on_right_arrow_press(self):
        pass

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_release(self):
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_release(self):
        pass

    def on_options_press(self):
        pass

    def on_options_release(self):
        pass


class Controller(Actions):

    EVENT_SIZE = struct.calcsize("LhBB")

    def __init__(self, interface, via_bluetoothctl=False):
        """
        Initiate controller instance that is capable of listening to all events on specified input interface
        :param interface: STRING aka /dev/input/js0 or any other PS4 Duelshock controller interface.
        :param via_bluetoothctl: BOOLEAN. If you are using ds4drv leave it set to False.
                                          If connecting your device using bluetoothctl cli set this to True.
        """
        Actions.__init__(self)
        self.stop = False
        self.interface = interface
        self.via_bluetoothctl = via_bluetoothctl

    def listen(self):

        def read_events():
            try:
                return _file.read(Controller.EVENT_SIZE)
            except IOError:
                print("Device not found / disconnected. Exiting.")
                exit(1)

        while not self.stop:
            try:
                _file = open(self.interface, "rb")
                event = read_events()
                while event:
                    (tv_sec, value, button_type, button_id) = struct.unpack("LhBB", event)
                    if button_id not in [6, 7, 8, 11, 12, 13]:
                        self.__event(button_id=button_id, button_type=button_type, value=value)
                    event = read_events()
            except KeyboardInterrupt:
                print("Exiting (Ctrl + C)")
                exit(1)

    def __event(self, button_id, button_type, value):

        # L joystick group #
        def L3_event():
            return button_type == 2 and button_id in [1, 0]

        def L3_at_rest():
            return button_id in [1, 0] and value == 0

        def L3_up():
            return button_id == 1 and value < 0

        def L3_down():
            return button_id == 1 and value > 0

        def L3_left():
            return button_id == 0 and value < 0

        def L3_right():
            return button_id == 0 and value > 0

        # R joystick group #
        def R3_event():
            if self.via_bluetoothctl:
                return button_type == 2 and button_id in [4, 3]
            return button_type == 2 and button_id in [5, 2]

        def R3_at_rest():
            if self.via_bluetoothctl:
                return button_id == 4 and button_type == 2 and value == -32767
            return button_id in [2, 5] and value == 0

        def R3_up():
            if self.via_bluetoothctl:
                return button_id == 4 and button_type == 2 and (value >= -32766)
            return button_id == 5 and value < 0

        def R3_down():
            if self.via_bluetoothctl:
                return button_id == 4 and button_type == 2 and (32767 >= value)
            return button_id == 5 and value > 0

        def R3_left():
            if self.via_bluetoothctl:
                return button_id == 3 and button_type == 2 and (value >= -32766)
            return button_id == 2 and value < 0

        def R3_right():
            if self.via_bluetoothctl:
                return button_id == 3 and button_type == 2 and (32767 >= value)
            return button_id == 2 and value > 0

        # Square / Triangle / Circle / X Button group #
        def circle_pressed():
            return button_id == 2 and button_type == 1 and value == 1

        def circle_released():
            return button_id == 2 and button_type == 1 and value == 0

        def x_pressed():
            return button_id == 1 and button_type == 1 and value == 1

        def x_release():
            return button_id == 1 and button_type == 1 and value == 0

        def triangle_pressed():
            return button_id == 3 and button_type == 1 and value == 1

        def triangle_released():
            return button_id == 3 and button_type == 1 and value == 0

        def square_pressed():
            return button_id == 0 and button_type == 1 and value == 1

        def square_released():
            return button_id == 0 and button_type == 1 and value == 0

        def options_pressed():
            return button_id == 9 and button_type == 1 and value == 1

        def options_released():
            return button_id == 9 and button_type == 1 and value == 0

        # N1 group #
        def L1_pressed():
            return button_id == 4 and button_type == 1 and value == 1

        def L1_released():
            return button_id == 4 and button_type == 1 and value == 0

        def R1_pressed():
            return button_id == 5 and button_type == 1 and value == 1

        def R1_released():
            return button_id == 5 and button_type == 1 and value == 0

        # N2 group #
        def L2_pressed():
            return button_id == 3 if not self.via_bluetoothctl else 2 and button_type == 2 and (32767 >= value >= -32766)

        def L2_released():
            return button_id == 3 if not self.via_bluetoothctl else 2 and button_type == 2 and value == -32767

        def R2_pressed():
            return button_id == 4 if not self.via_bluetoothctl else 5 and button_type == 2 and (32767 >= value >= -32766)

        def R2_released():
            return button_id == 4 if not self.via_bluetoothctl else 5 and button_type == 2 and value == -32767

        # up / down arrows #
        def up_arrow_press():
            return button_id == 10 and button_type == 2 and value == -32767

        def down_arrow_press():
            return button_id == 10 and button_type == 2 and value == 32767

        def up_down_arrow_release():
            # arrow buttons on release are not distinguishable and if you think about it,
            # they are following same principle as the joystick buttons which only have 1
            # state at rest which is shared between left/ right / up /down inputs
            return button_id == 10 and button_type == 2 and value == 0

        # left / right arrows #
        def left_arrow_press():
            return button_id == 9 and button_type == 2 and value == -32767

        def right_arrow_press():
            return button_id == 9 and button_type == 2 and value == 32767

        def left_right_arrow_release():
            # arrow buttons on release are not distinguishable and if you think about it,
            # they are following same principle as the joystick buttons which only have 1
            # state at rest which is shared between left/ right / up /down inputs
            return button_id == 9 and button_type == 2 and value == 0

        if R3_event():
            if R3_at_rest():
                self.on_R3_release()
            elif R3_right():
                self.on_R3_right(value)
            elif R3_left():
                self.on_R3_left(value)
            elif R3_up():
                self.on_R3_up(value)
            elif R3_down():
                self.on_R3_down(value)
        elif L3_event():
            if L3_at_rest():
                self.on_L3_release()
            elif L3_up():
                self.on_L3_up(value)
            elif L3_down():
                self.on_L3_down(value)
            elif L3_left():
                self.on_L3_left(value)
            elif L3_right():
                self.on_L3_right(value)
        elif circle_pressed():
            self.on_circle_press()
        elif circle_released():
            self.on_circle_release()
        elif x_pressed():
            self.on_x_press()
        elif x_release():
            self.on_x_release()
        elif triangle_pressed():
            self.on_triangle_press()
        elif triangle_released():
            self.on_triangle_release()
        elif square_pressed():
            self.on_square_press()
        elif square_released():
            self.on_square_release()
        elif L1_pressed():
            self.on_L1_press()
        elif L1_released():
            self.on_L1_release()
        elif L2_pressed():
            self.on_L2_press(value)
        elif L2_released():
            self.on_L2_release()
        elif R1_pressed():
            self.on_R1_press()
        elif R1_released():
            self.on_R1_release()
        elif R2_pressed():
            self.on_R2_press(value)
        elif R2_released():
            self.on_R2_release()
        elif options_pressed():
            self.on_options_press()
        elif options_released():
            self.on_options_release()
        elif left_right_arrow_release():
            self.on_left_right_arrow_release()
        elif up_down_arrow_release():
            self.on_up_down_arrow_release()
        elif left_arrow_press():
            self.on_left_arrow_press()
        elif right_arrow_press():
            self.on_right_arrow_press()
        elif up_arrow_press():
            self.on_up_arrow_press()
        elif down_arrow_press():
            self.on_down_arrow_press()
