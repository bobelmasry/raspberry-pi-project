import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# Create a CvBridge instance to convert between ROS Image messages and OpenCV images
bridge = CvBridge()

# Callback function to be called when a depth image is received
def depth_callback(data):
    # Convert ROS Image to OpenCV format
    depth_image = bridge.imgmsg_to_cv2(data)

    # Extract depth value for a specific pixel (e.g., pixel at row=100, col=150)
    row, col = 100, 150
    depth_value = depth_image[row, col]

    # Assuming depth is in millimeters, convert to meters
    depth_meters = depth_value / 1000.0

    # Log the distance information to the console
    rospy.loginfo(f"Distance to pixel ({row}, {col}): {depth_meters} meters")

# Main function to initialize the ROS node and subscribe to the depth image topic
def main():
    # Initialize the ROS node with the name 'depth_measurement_node'
    rospy.init_node('depth_measurement_node', anonymous=True)

    # Subscribe to the depth image topic ('/camera/depth/image_rect_raw') and specify the callback function
    rospy.Subscriber('/camera/depth/image_rect_raw', Image, depth_callback)

    # Keep the program running until the node is shut down
    rospy.spin()

# Entry point for the script
if __name__ == '__main__':
    main()
