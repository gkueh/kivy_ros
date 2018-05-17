import rospy
from std_msgs.msg import String

def kivy_listener():

	rospy.init_node('listener', anonymous=True)
	msg = rospy.wait_for_message("time", String)

	return msg

if __name__ == '__main__':
	kivy_listener()