import keyboard
from gpiozero import Motor
from time import sleep

top_left = Motor(forward = 4)
top_right = Motor(forward= 17)
rear_left = Motor(forward= 27)
rear_right = Motor(forward= 22)



while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        top_left.forward()
        top_right.forward()
        rear_left.forward()
        rear_right.forward()
        print('forward')
        sleep(.03)


    elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
        top_right.forward()
        rear_right.forward()
        rear_left.forward()
        print('left')
        sleep(.03)


    elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
        top_left.forward()
        rear_left.forward()
        rear_right.forward()
        print('right')
        sleep(.03)
    else: pass