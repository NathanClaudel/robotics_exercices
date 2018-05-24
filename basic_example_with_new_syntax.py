#import the library

from robot import Robot
from AX12 import AX12
from inputs import get_mouse
from time import sleep


# ---------------------------   ROBOT CONSTRUCTION   --------------------------#
#creates the robot skeleton
r = Robot()

#adds motors to the robot skeleton
r.add_object(AX12(135), "motorY")
r.add_object(AX12(141), "motorX")


# -------------------------   SEQUENCE DEFINITION ----------------------------#

def follow_scroll():
    position = 0

    while 1:
        sleep(0.001)
        events = get_mouse()
        for state, code in [(event.state, event.code) for event in events if event.code in ['REL_X', 'REL_Y']]:
            if(code == 'REL_X'):
                try:
                    r.motorX.turn(-state//2)
                except:
                    pass
            else:
                try:
                    r.motorY.turn(-state//2)
                except:
                    pass

#defines a sequence of actions
#note that the sequence is only defined and not run (for the moment)
r.add_sequence("seq_1")

#first block of actions; all actions of a block are performed simultaneously
#the "wait" defines the end of the block
#and it waits :
# 	until max_delay seconds are elapsed
# 	OR until n_callbacks actions of this block are done
#you MUST specify where the definition of the sequence ends
# so the following line means "end of seq_1 definition"
r.sequence_done()



# --------------------- RUNNING ! ------------------------------------------#

# We run the sequence we defined above
r.start_sequence("seq_1")


# We wait the end of the sequence execution
r.wait_sequence()

follow_scroll()

#close the thread
r.stop()
