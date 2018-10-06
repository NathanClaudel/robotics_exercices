STRAIGHT  = -45
AMPLITUDE = -10
STICK_MAX = 3000

#import evdev
from evdev import InputDevice, categorize, ecodes
from AX12 import AX12

direction = AX12(172)

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    type, value = str(categorize(event)).split()[-1], event.value
    if(type == 'ABS_X'):
        direction.move(int(value * AMPLITUDE / STICK_MAX))
