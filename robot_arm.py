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

claw_position = 0
r.z_axis.turn(0)
r.y_axis.turn(0)
r.claw.turn(0)

while True:
    events = get_mouse()
    for event in events:
	try:
            if event.code == 'REL_WHEEL':
                claw_position += 10*event.state
		r.claw.move(claw_position)
            elif event.code == 'REL_X':
                r.z_axis.turn(-event.state)
            elif event.code == 'REL_Y':
                r.y_axis.turn(event.state)
        except:
            pass
