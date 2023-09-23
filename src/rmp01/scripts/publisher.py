#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def pub():
    rospy.init_node('publisher')
    publisher_details = rospy.Publisher('user_input', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = str(input("What shape to play out?"))
        publisher_details.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        pass