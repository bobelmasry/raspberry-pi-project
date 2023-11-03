from gpiozero import Motor

# Initialize motors
top_left = Motor(forward=4, backward=22)
top_right = Motor(forward=17, backward=23)
bottom_left = Motor(forward=5, backward=6)
bottom_right = Motor(forward=26, backward=16)

# Function to stop all motors
def stop_motors():
    top_left.stop()
    top_right.stop()
    bottom_left.stop()
    bottom_right.stop()

while True:
    # Prompt the user for a command
    command = input("Enter a command (w/a/d/q to quit): ")

    if command == 'w':
        top_left.forward()
        top_right.forward()
        bottom_left.forward()
        bottom_right.forward()
    elif command == 'a':
        top_right.forward()
        bottom_left.forward()
        bottom_right.forward()
    elif command == 'd':
        top_left.forward()
        bottom_left.forward()
        bottom_right.forward()
        
    elif command == 's':
        top_left.backward()
        top_right.backward()
        bottom_left.backward()
        bottom_right.backward()
        
    elif command == 'q':
        # Stop all motors and exit the loop
        stop_motors()
        break
    else:
        # Invalid input, stop all motors
        stop_motors()

# Stop all motors before exiting
stop_motors()

