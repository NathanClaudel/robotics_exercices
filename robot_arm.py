#import the library

from robot import Robot
from AX12 import AX12
from inputs import get_mouse

# ---------------------------   ROBOT CONSTRUCTION   --------------------------#
#creates the robot skeleton
r = Robot()

#adds motors to the robot skeleton
r.add_object(AX12(25), "z_axis")
r.add_object(AX12(142), "y_axis")
r.add_object(AX12(121), "claw")

while True:
    event = get_mouse()
    for event in events:
        try:
            if event.code == REL_WHEEL:
                r.claw.turn(event.state)
            elif event.code == REL_X:
                r.z_axis.turn(event.state)
            elif event.code == REL_Y:
                r.axis.turn(event.state)
        except:
            pass
