'''
from inputs import devices

for device in devices:

    print(device)

'''
from inputs import get_mouse
while 1:
     events = get_mouse()
     for event in events:
        print(event.ev_type, event.code, event.state)
