#!/usr/bin/env python3 
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)
    print(f"data is {data.data}")


def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('user_input', String, callback=callback)
    rospy.spin()

if __name__ == "__main__":
    listener()