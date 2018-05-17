import rospy
from std_msgs.msg import String
import time

def time_node():
    pub = rospy.Publisher('time', String, queue_size=10)
    rospy.init_node('time_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        time_str = str(rospy.get_time())
        # rospy.loginfo(hello_str)
        pub.publish(time.asctime())
        rate.sleep()

if __name__ == '__main__':
    try:
        time_node()
    except rospy.ROSInterruptException:
        pass