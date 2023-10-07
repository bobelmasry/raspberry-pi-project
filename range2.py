from gpiozero import Motor
from pynput import keyboard
from time import sleep
import threading

# Define motor pins
top_left = Motor(forward=4, backward=22)
top_right = Motor(forward=17, backward=23)
bottom_left = Motor(forward=5, backward=6)
bottom_right = Motor(forward=26, backward=16)

# Initialize a list to store the keys currently being pressed
keys_pressed = []

def on_key_release(key):
    try:
        # Remove the released key from the list
        keys_pressed.remove(key.char)
    except (ValueError, AttributeError):
        pass

def on_key_press(key):
    try:
        # Add the pressed key to the list
        keys_pressed.append(key.char)
        process_keys()
    except AttributeError:
        pass

def process_keys():
    # Check the keys being pressed and control motors accordingly
    if 'w' in keys_pressed:
        top_left.forward()
        top_right.forward()
        bottom_left.forward()
        bottom_right.forward()
    elif 'a' in keys_pressed:
        top_right.forward()
        bottom_left.forward()
        bottom_right.forward()
    elif 'd' in keys_pressed:
        top_left.forward()
        bottom_left.forward()
        bottom_right.forward()
    else:
        # Stop all motors if no keys are pressed
        top_left.stop()
        top_right.stop()
        bottom_left.stop()
        bottom_right.stop()

# Create separate threads for keyboard input and motor control
keyboard_thread = threading.Thread(target=listen_keyboard)
motor_thread = threading.Thread(target=process_keys)

def listen_keyboard():
    # Listen to keyboard input
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()

# Start both threads
keyboard_thread.start()
motor_thread.start()

# Wait for the threads to finish
keyboard_thread.join()
motor_thread.join()
