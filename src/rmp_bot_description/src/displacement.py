#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry

# Subscribe to /odom topic.
def callback(data):
    #rospy.loginfo(data)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    print(f"The current displacement is x:{x} y:{y}")

def odom_listener():
    rospy.init_node("displacement",anonymous=True)
    rospy.Subscriber(name='odom',data_class=Odometry, callback=callback)
    rospy.spin()
    

if __name__ == "__main__":
    try:
        odom_listener()
    except KeyboardInterrupt:
        rospy.loginfo("Shutting down !!!")
