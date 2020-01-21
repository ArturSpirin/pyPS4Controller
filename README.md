# pyPS4Controller
##

pyPS4Controller is a light module designed to provide hooks for PS4 Controller using Python on Linux.

## Installation
`pip install pyPS4Controller`

## Usage
```python
from pyPS4Controller import Controller

class MyController(Controller):  # create a custom class for your controller and subclass Controller
    """
    If we want to bind an action to the X button on the controller, we need to override its respective methods.
    
    Some of the buttons have a binary On/Off state. For example the X, Circle, Square, and Triangle buttons.
    When overriding their respective methods there are no args in the function signature.

    Some controls like the L2, L3, R2 and R3 have a variable On state.
    When overriding their respective method, there is a value argument in the function signature 
    which indicates the degree of the input.
    """    
    def on_x_press(self):
        # Input any code that you want to run when X is pressed
        print("X pressed!")

    def on_x_release(self):
        # Input any code that you want to run when X is released
        print("X released!")

    def on_L3_up(self, value):
        # Input any code that you want to run when left joystick (L3) is pushed up
        # value will indicate the degree of how far the joystick is pushed
        print(f"L3 pushed up: {value}")

    def on_L3_release(self):
        # Input any code that you want to run when left joystick (L3) is back to its resting state
        print("L3 at rest!")

# now make sure the controller is paired over the Bluetooth and turn on the listener
MyController(interface="/dev/input/js0").listen()
```

## Pair PS4 Controller with the Raspberry Pi
See detailed instructions [here](https://github.com/macunixs/dualshock4-pi)
