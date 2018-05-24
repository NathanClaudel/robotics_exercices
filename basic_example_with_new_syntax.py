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


# -------------------------   SEQUENCE DEFINITION ----------------------------#

def follow_scroll():
    position = 0

    while 1:
        sleep(0.001)
        events = get_mouse()
        for state in [event.state for event in events if event.code == "REL_X"]:

            try:
                if state != 0 :
                    r.motor.turn(10)

            except:
                pass




follow_scroll()
