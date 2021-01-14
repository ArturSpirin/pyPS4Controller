from pyPS4Controller.event_mapping.DefaultMapping import DefaultMapping


class Mapping3Bh2b(DefaultMapping):

    def __init__(self, button_id, button_type, value, connecting_using_ds4drv, overflow, debug=False):
        """
        For 3Bh2b format, all the data that can distinguish buttons in in the overflow tuple
        :param button_id: Just a placeholder in the signature
        :param button_type: Just a placeholder in the signature
        :param value:  Just a placeholder in the signature
        :param connecting_using_ds4drv: Just a placeholder in the signature
        :param overflow: TUPLE aka (0, 1, 8) aka (value, type_id, button_id)
        :param debug: BOOLEAN
        """
        self.button_id = overflow[2]
        self.button_type = overflow[1]
        self.value = overflow[0]
        self.connecting_using_ds4drv = connecting_using_ds4drv
        self.overflow = overflow
        if debug:
            print("button_id: {} button_type: {} value: {} overflow: {}"
                  .format(self.button_id, self.button_type, self.value, self.overflow))
        DefaultMapping.__init__(self, self.button_id, self.button_type, self.value, connecting_using_ds4drv)

    # Square / Triangle / Circle / X Button group #
    def circle_pressed(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 1

    def circle_released(self):
        return self.button_id == 1 and self.button_type == 1 and self.value == 0

    def x_pressed(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 1

    def x_released(self):
        return self.button_id == 0 and self.button_type == 1 and self.value == 0

    def triangle_pressed(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 1

    def triangle_released(self):
        return self.button_id == 2 and self.button_type == 1 and self.value == 0

    def square_pressed(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 1

    def square_released(self):
        return self.button_id == 3 and self.button_type == 1 and self.value == 0
