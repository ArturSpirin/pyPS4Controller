

class DefaultMapping:

    def __init__(self, button_id, button_type, value, connecting_using_ds4drv, overflow=None, debug=False):
        """
        DEFAULT MAPPING
        :param button_id: INT
        :param button_type: INT
        :param value: INT
        :param connecting_using_ds4drv: BOOLEAN
        :param overflow: TUPLE, carries values that overflowed during unpacking
        :param debug: BOOLEAN
        """
        self.button_id = button_id
        self.button_type = button_type
        self.value = value
        self.connecting_using_ds4drv = connecting_using_ds4drv
        self.overflow = overflow
        if debug:
            print("button_id: {} button_type: {} value: {} overflow: {}"
                  .format(self.button_id, self.button_type, self.value, self.overflow))

    # L joystick group #
    def L3_event(self):  # L3 has the same mapping on ds4drv as it does when connecting  to bluetooth directly
        return self.button_type == 2 and self.button_id in [1, 0]

    def L3_y_at_rest(self):
        return self.button_id in [1] and self.value == 0

    def L3_x_at_rest(self):
        return self.button_id in [0] and self.value == 0

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

    def R3_y_at_rest(self):
        if not self.connecting_using_ds4drv:
            return self.button_id in [4] and self.value == 0
        return self.button_id in [2] and self.value == 0

    def R3_x_at_rest(self):
        if not self.connecting_using_ds4drv:
            return self.button_id in [3] and self.value == 0
        return self.button_id in [5] and self.value == 0

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
