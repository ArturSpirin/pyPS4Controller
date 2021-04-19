""" Simple module for testing logging in controller module. """
import logging
import sys

from pyPS4Controller.controller import Controller

logging.basicConfig(
    stream=sys.stdout,
    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)
pyps4logger = logging.getLogger("pyPS4Controller.controller")
pyps4logger.setLevel(logging.DEBUG)


def connect():
    # any code you want to run during initial connection with the controller
    logger.debug("gamepad connected")


def disconnect():
    # any code you want to run during loss of connection with the controller or keyboard interrupt
    logger.debug("gamepad disconnected")


class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


controller = MyController(
    interface="/dev/input/js0", event_format="3Bh2b", connecting_using_ds4drv=False
)
controller.listen()
