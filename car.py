STRAIGHT  = -45
AMPLITUDE = 30
STICK_MAX = 30000
TRIGGER_MAX = 255
SPEAR_HORIZ = 132
SPEAR_MIN  = 20
SPEAR_MAX = 150
SPEAR_SPEED = 0.5


import evdev
from evdev import InputDevice, categorize, ecodes
from AX12 import AX12

direction = AX12(25)
speed = AX12(172)
death_engine = AX12(142)
balloon = AX12(143)

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    type, value = str(categorize(event)).split()[-1], event.value
    print type, value
    try:
        if(type == 'ABS_X'):
            direction.move(int(value) * AMPLITUDE / STICK_MAX + STRAIGHT)
        elif(type == 'ABS_RZ'):
            speed.turn(-100*int(value)/TRIGGER_MAX)
        elif(type == 'ABS_Z'):
            speed.turn( 100*int(value)/TRIGGER_MAX)
        elif(type == 'ABS_RY'):
            death_engine.turn(SPEAR_SPEED * int(value) / 300)

            pos = death_engine.get_position()
            print(pos)
            '''
            if (pos<SPEAR_MIN) :
                death_engine.move(SPEAR_MIN)
            if (pos>SPEAR_MAX):
                death_engine.move(SPEAR_MAX)
            '''
        elif(type == 'ABS_HAT0Y'):
            print("I did receive that..")
            ballon.turn(-1)
            if value=="1":
                print("ok1")
                balloon.turn(10)
            if value==-1:
                print("ok2")
                ballon.turn(-10)
    except:
        pass
