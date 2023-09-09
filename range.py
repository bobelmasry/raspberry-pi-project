import keyboard
from gpiozero import Motor, LED
from time import sleep

top_left = Motor(forward = 4, backward=22) #blue and grey
top_right = Motor(forward= 17, backward=23) # yellow and purple
bottom_left = LED(6)
bottom_right = LED(16)



while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        top_left.forward()
        top_right.forward()
        bottom_left.on()
        bottom_right.on()
        print('forward')
        sleep(.03)
        top_left.stop()
        top_right.stop()
        bottom_left.off()
        bottom_right.off()


    elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
        top_right.forward()
        bottom_left.on()
        bottom_right.on()
        print('left')
        sleep(.03)
        top_right.stop()
        bottom_left.off()
        bottom_right.off()


    elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
        top_left.forward()
        bottom_left.on()
        bottom_right.on()
        print('right')
        sleep(.03)
        top_left.stop()
        bottom_left.off()
        bottom_right.off()
    else: pass