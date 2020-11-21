import logging

from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


logging.basicConfig(level=logging.DEBUG)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.trace_raw_events = False
controller.listen()
