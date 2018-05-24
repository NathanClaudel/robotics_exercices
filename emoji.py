#import the library

from robot import Robot
from AX12 import AX12
from inputs import get_mouse
from time import sleep


# ---------------------------   ROBOT CONSTRUCTION   --------------------------#
#creates the robot skeleton
r = Robot()

#adds motors to the robot skeleton
r.add_object(AX12(174), "motor")
r.motor.set_speed(100)
r.motor.set_torque(100)


# -------------------------   SEQUENCE DEFINITION ----------------------------#

while 1:
    n = input()
    if n=="quit":
        break

    if n=='turn':
        r.motor.turn(100)
    else:
        r.motor.move(n)

#close the thread
r.stop()
