import keyboard
from gpiozero import LED

led = LED(26)


while True:
    if keyboard.read_key()=="h":
        print('On!')
        led.on()
    elif keyboard.read_key()=="l":
        led.off()
        print('Off!')