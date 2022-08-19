import keyboard
from gpiozero import LED
from time import sleep

top_left = LED(4)
top_right = LED(17)
rear_left = LED(27)
rear_right = LED(22)



while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        top_left.on()
        top_right.on()
        rear_left.on()
        rear_right.on()
        print('foreward')
        sleep(.03)
        top_left.off()
        top_right.off()
        rear_left.off()
        rear_right.off()


    elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
        top_right.on()
        rear_right.on()
        rear_left.on()
        print('left')
        sleep(.03)
        top_right.off()
        rear_right.off()
        rear_left.off()


    elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
        top_left.on()
        rear_left.on()
        rear_right.on()
        print('right')
        sleep(.03)
        top_left.off()
        rear_left.off()
        rear_right.off()
    else: pass

