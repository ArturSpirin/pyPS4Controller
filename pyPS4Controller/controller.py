import os
import struct
import time


class Event:

    def __init__(self, button_id, button_type, value, connecting_using_ds4drv):

        self.button_id = button_id
        self.button_type = button_type
        self.value = value
        self.connecting_using_ds4drv = connecting_using_ds4drv

    # L joystick group #
    def L3_event(self):  # L3 has the same mapping on ds4drv as it does when connecting  to bluetooth directly
        return self.button_type == 2 and self.button_id in [1, 0]

    def L3_at_rest(self):
        return self.button_id in [1, 0] and self.value == 0

    def L3_up(self):
        return self.button_id == 1 and self.value < 0

    def L3_down(self):
        return self.button_id == 1 and self.value > 0

    def L3_left(self):
        return self.button_id == 0 and self.value < 0

    def L3_right(self):
        return self.button_id == 0 and self.value > 0

    def L3_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 11 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def L3_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 11 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv

    # R joystick group #
    def R3_event(self):
        if not self.connecting_using_ds4drv:
            return self.button_type == 2 and self.button_id in [4, 3]
        return self.button_type == 2 and self.button_id in [5, 2]

    def R3_at_rest(self):
        if not self.connecting_using_ds4drv:
            return self.button_id in [4, 3] and self.value == 0
        return self.button_id in [2, 5] and self.value == 0

    def R3_up(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 4 and self.value < 0
        return self.button_id == 5 and self.value < 0

    def R3_down(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 4 and self.value > 0
        return self.button_id == 5 and self.value > 0

    def R3_left(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 3 and self.value < 0
        return self.button_id == 2 and self.value < 0

    def R3_right(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 3 and self.value > 0
        return self.button_id == 2 and self.value > 0

    def R3_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 12 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def R3_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 12 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv

    # Square / Triangle / Circle / X Button group #
    def circle_pressed(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 1

    def circle_released(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 0

    def x_pressed(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 1

    def x_released(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 0

    def triangle_pressed(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 1

    def triangle_released(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 0

    def square_pressed(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 1

    def square_released(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 0

    def options_pressed(self):
        return self.button_id == 9 and self.button_type == 1 and self.value == 1

    def options_released(self):
        return self.button_id == 9 and self.button_type == 1 and self.value == 0

    def share_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 8 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def share_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 8 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv

    # N1 group #
    def L1_pressed(self):
        return self.button_id == 4 and self.button_type == 1 and self.value == 1

    def L1_released(self):
        return self.button_id == 4 and self.button_type == 1 and self.value == 0

    def R1_pressed(self):
        return self.button_id == 5 and self.button_type == 1 and self.value == 1

    def R1_released(self):
        return self.button_id == 5 and self.button_type == 1 and self.value == 0

    # N2 group #
    def L2_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 2 and self.button_type == 2 and (32767 >= self.value >= -32766)
        return self.button_id == 3 and self.button_type == 2 and (32767 >= self.value >= -32766)

    def L2_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 2 and self.button_type == 2 and self.value == -32767
        return self.button_id == 3 and self.button_type == 2 and self.value == -32767

    def R2_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 5 and self.button_type == 2 and (32767 >= self.value >= -32766)
        return self.button_id == 4 and self.button_type == 2 and (32767 >= self.value >= -32766)

    def R2_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 5 and self.button_type == 2 and self.value == -32767
        return self.button_id == 4 and self.button_type == 2 and self.value == -32767

    # up / down arrows #
    def up_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 7 and self.button_type == 2 and self.value == -32767
        return self.button_id == 10 and self.button_type == 2 and self.value == -32767

    def down_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 7 and self.button_type == 2 and self.value == 32767
        return self.button_id == 10 and self.button_type == 2 and self.value == 32767

    def up_down_arrow_released(self):
        # arrow buttons on release are not distinguishable and if you think about it,
        # they are following same principle as the joystick buttons which only have 1
        # state at rest which is shared between left/ right / up /down inputs
        if not self.connecting_using_ds4drv:
            return self.button_id == 7 and self.button_type == 2 and self.value == 0
        return self.button_id == 10 and self.button_type == 2 and self.value == 0

    # left / right arrows #
    def left_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 6 and self.button_type == 2 and self.value == -32767
        return self.button_id == 9 and self.button_type == 2 and self.value == -32767

    def right_arrow_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 6 and self.button_type == 2 and self.value == 32767
        return self.button_id == 9 and self.button_type == 2 and self.value == 32767

    def left_right_arrow_released(self):
        # arrow buttons on release are not distinguishable and if you think about it,
        # they are following same principle as the joystick buttons which only have 1
        # state at rest which is shared between left/ right / up /down inputs
        if not self.connecting_using_ds4drv:
            return self.button_id == 6 and self.button_type == 2 and self.value == 0
        return self.button_id == 9 and self.button_type == 2 and self.value == 0

    def playstation_button_pressed(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 10 and self.button_type == 1 and self.value == 1
        return False  # cant identify this event when connected through ds4drv

    def playstation_button_released(self):
        if not self.connecting_using_ds4drv:
            return self.button_id == 10 and self.button_type == 1 and self.value == 0
        return False  # cant identify this event when connected through ds4drv


class Actions:
    """
    Actions are inherited in the Controller class.
    In order to bind to the controller events, subclass the Controller class and
    override desired action events in this class.
    """
    def __init__(self):
        return

    def on_x_press(self):
        print("on_x_press")

    def on_x_release(self):
        print("on_x_release")

    def on_triangle_press(self):
        print("on_triangle_press")

    def on_triangle_release(self):
        print("on_triangle_release")

    def on_circle_press(self):
        print("on_circle_press")

    def on_circle_release(self):
        print("on_circle_release")

    def on_square_press(self):
        print("on_square_press")

    def on_square_release(self):
        print("on_square_release")

    def on_L1_press(self):
        print("on_L1_press")

    def on_L1_release(self):
        print("on_L1_release")

    def on_L2_press(self, value):
        print("on_L2_press: {}".format(value))

    def on_L2_release(self):
        print("on_L2_release")

    def on_R1_press(self):
        print("on_R1_press")

    def on_R1_release(self):
        print("on_R1_release")

    def on_R2_press(self, value):
        print("on_R2_press: {}".format(value))

    def on_R2_release(self):
        print("on_R2_release")

    def on_up_arrow_press(self):
        print("on_up_arrow_press")

    def on_up_down_arrow_release(self):
        print("on_up_down_arrow_release")

    def on_down_arrow_press(self):
        print("on_down_arrow_press")

    def on_left_arrow_press(self):
        print("on_left_arrow_press")

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")

    def on_right_arrow_press(self):
        print("on_right_arrow_press")

    def on_L3_up(self, value):
        print("on_L3_up: {}".format(value))

    def on_L3_down(self, value):
        print("on_L3_down: {}".format(value))

    def on_L3_left(self, value):
        print("on_L3_left: {}".format(value))

    def on_L3_right(self, value):
        print("on_L3_right: {}".format(value))

    def on_L3_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_at_rest")

    def on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_L3_press")

    def on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_L3_release")

    def on_R3_up(self, value):
        print("on_R3_up: {}".format(value))

    def on_R3_down(self, value):
        print("on_R3_down: {}".format(value))

    def on_R3_left(self, value):
        print("on_R3_left: {}".format(value))

    def on_R3_right(self, value):
        print("on_R3_right: {}".format(value))

    def on_R3_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        print("on_R3_at_rest")

    def on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_R3_press")

    def on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_R3_release")

    def on_options_press(self):
        print("on_options_press")

    def on_options_release(self):
        print("on_options_release")

    def on_share_press(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_share_press")

    def on_share_release(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_share_release")

    def on_playstation_button_press(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_playstation_button_press")

    def on_playstation_button_release(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_playstation_button_release")


class Controller(Actions):

    EVENT_SIZE = struct.calcsize("LhBB")

    def __init__(self, interface, connecting_using_ds4drv=True, event_definition=None):
        """
        Initiate controller instance that is capable of listening to all events on specified input interface
        :param interface: STRING aka /dev/input/js0 or any other PS4 Duelshock controller interface.
                          You can see all available interfaces with a command "ls -la /dev/input/"
        :param connecting_using_ds4drv: BOOLEAN. If you are connecting your controller using ds4drv, then leave it set
                                                 to True. Otherwise if you are connecting directly via directly via
                                                 bluetooth/bluetoothctl, set it to False otherwise the controller
                                                 button mapping will be off.
        """
        Actions.__init__(self)
        self.stop = False
        self.interface = interface
        self.connecting_using_ds4drv = connecting_using_ds4drv
        self.debug = False  # If you want to see raw event stream, set this to True.
        self.black_listed_buttons = []  # set a list of blocked buttons if you dont want to process their events
        if self.connecting_using_ds4drv and event_definition is None:
            # when device is connected via ds4drv its sending hundreds of events for those button IDs
            # thus they are blacklisted by default. Feel free to adjust this list to your linking when sub-classing
            self.black_listed_buttons += [6, 7, 8, 11, 12, 13]
        self.event_definition = event_definition if event_definition else Event

    def listen(self, timeout=30):
        """
        Start listening for events on a given self.interface
        :param timeout: INT, seconds. How long you want to wait for the self.interface.
                        This allows you to start listening and connect your controller after the fact.
                        If self.interface does not become available in N seconds, the script will exit with exit code 1.
        :return: None
        """

        def wait_for_interface():
            print("Waiting for interface: {} to become available . . .".format(self.interface))
            for i in range(timeout):
                if os.path.exists(self.interface):
                    print("Successfully bound to: {}.".format(self.interface))
                    return
                time.sleep(1)
            print("Timeout({} sec). Interface not available.".format(timeout))
            exit(1)

        def read_events():
            try:
                return _file.read(Controller.EVENT_SIZE)
            except IOError:
                print("Interface lost. Device disconnected?")
                exit(1)

        wait_for_interface()
        while not self.stop:
            try:
                _file = open(self.interface, "rb")
                event = read_events()
                while event:
                    (tv_sec, value, button_type, button_id) = struct.unpack("LhBB", event)
                    if self.debug:
                        print("button_id: {} button_type: {} value: {}".format(button_id, button_type, value))
                    if button_id not in self.black_listed_buttons:
                        self.__handle_event(button_id=button_id, button_type=button_type, value=value)
                    event = read_events()
            except KeyboardInterrupt:
                print("\nExiting (Ctrl + C)")
                exit(1)

    def __handle_event(self, button_id, button_type, value):

        event = self.event_definition(button_id=button_id,
                                      button_type=button_type,
                                      value=value,
                                      connecting_using_ds4drv=self.connecting_using_ds4drv)

        if event.R3_event():
            if event.R3_at_rest():
                self.on_R3_at_rest()
            elif event.R3_right():
                self.on_R3_right(value)
            elif event.R3_left():
                self.on_R3_left(value)
            elif event.R3_up():
                self.on_R3_up(value)
            elif event.R3_down():
                self.on_R3_down(value)
        elif event.L3_event():
            if event.L3_at_rest():
                self.on_L3_at_rest()
            elif event.L3_up():
                self.on_L3_up(value)
            elif event.L3_down():
                self.on_L3_down(value)
            elif event.L3_left():
                self.on_L3_left(value)
            elif event.L3_right():
                self.on_L3_right(value)
        elif event.circle_pressed():
            self.on_circle_press()
        elif event.circle_released():
            self.on_circle_release()
        elif event.x_pressed():
            self.on_x_press()
        elif event.x_released():
            self.on_x_release()
        elif event.triangle_pressed():
            self.on_triangle_press()
        elif event.triangle_released():
            self.on_triangle_release()
        elif event.square_pressed():
            self.on_square_press()
        elif event.square_released():
            self.on_square_release()
        elif event.L1_pressed():
            self.on_L1_press()
        elif event.L1_released():
            self.on_L1_release()
        elif event.L2_pressed():
            self.on_L2_press(value)
        elif event.L2_released():
            self.on_L2_release()
        elif event.R1_pressed():
            self.on_R1_press()
        elif event.R1_released():
            self.on_R1_release()
        elif event.R2_pressed():
            self.on_R2_press(value)
        elif event.R2_released():
            self.on_R2_release()
        elif event.options_pressed():
            self.on_options_press()
        elif event.options_released():
            self.on_options_release()
        elif event.left_right_arrow_released():
            self.on_left_right_arrow_release()
        elif event.up_down_arrow_released():
            self.on_up_down_arrow_release()
        elif event.left_arrow_pressed():
            self.on_left_arrow_press()
        elif event.right_arrow_pressed():
            self.on_right_arrow_press()
        elif event.up_arrow_pressed():
            self.on_up_arrow_press()
        elif event.down_arrow_pressed():
            self.on_down_arrow_press()
        elif event.playstation_button_pressed():
            self.on_playstation_button_press()
        elif event.playstation_button_released():
            self.on_playstation_button_release()
        elif event.share_pressed():
            self.on_share_press()
        elif event.share_released():
            self.on_share_release()
        elif event.R3_pressed():
            self.on_R3_press()
        elif event.R3_released():
            self.on_R3_release()
        elif event.L3_pressed():
            self.on_L3_press()
        elif event.L3_released():
            self.on_L3_release()
