#!/usr/bin/env python3
import rospy
from timeit import default_timer as timer
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from argparse import ArgumentParser
from time import sleep
from math import radians
from std_srvs.srv import Empty
PI = 3.1415926535897

def user_input_listener():
    rospy.init_node('turtle_move', anonymous=True)
    rospy.Subscriber('user_input', String,callback=turtle_move)
    #rospy.Subscriber('user_input', String,callback=callback)
    rospy.spin()

def reset_turtlesim():
    clear_bg = rospy.ServiceProxy("/reset", Empty)
    clear_bg()

def turtle_move(data):
    shape = data.data
    print("### Printing new shape ###")
    publisher= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    velocity = Twist()
    reset_turtlesim()
    initial_x = 5.544 
    initial_y = 5.544 
    if(shape == 'c'):
        # Add the functions to call the shape movement here.
        start = timer()
        elapsed=0
        while(elapsed < 10):
            velocity.linear.x = 1
            velocity.linear.y = 0
            velocity.linear.z = 0
            velocity.angular.x = 0
            velocity.angular.y = 0
            velocity.angular.z = 1
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            elapsed = timer() - start

    elif(shape == 's'):
        # Move forward.
        start = timer()
        elapsed=0
        while(elapsed < 10):
            velocity.linear.x=3
            velocity.angular.z=0
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(.5)

            # Turn 90 Degrees.
            velocity.linear.x=0
            velocity.angular.z=PI/2
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)
            elapsed = timer() - start

    elif(shape == 'r'):
        start = timer()
        elapsed=0
        while(elapsed < 15):
            # Move forward.
            velocity.linear.x=2
            velocity.angular.z=0
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(0.5)

            # Turn 90 Degrees.
            velocity.linear.x=0
            velocity.angular.z=PI/2
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)

            #Move forward
            velocity.linear.x=4
            velocity.angular.z=0
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(0.5)

            # Turn 90 degrees
            velocity.linear.x=0
            velocity.angular.z=PI/2
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)
            elapsed = timer() - start


    elif(shape == 'p'):
        start = timer()
        elapsed=0
        while(elapsed < 25):
            rate.sleep()
            # Move forward.
            velocity.linear.x=1
            velocity.angular.z=0
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)

            # Turn 72 degrees
            velocity.linear.x=0
            velocity.angular.z=radians(108)
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)

            #Move forward
            velocity.linear.x=1
            velocity.angular.z=0
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)

            # Turn 90 degrees
            velocity.linear.x=0
            velocity.angular.z=radians(-36)
            publisher.publish(velocity)
            rospy.loginfo(velocity)
            sleep(1)

            elapsed = timer() - start

    elif (shape == 'x'):
        print("Resetting !!!")
        reset_turtlesim()
    else :
        print("Invalid argument!!")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-s','--shape', choices=['s','c','r','p'], default="c")
    args, unknown = parser.parse_known_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    try:
        user_input_listener()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node Terminated !!!")
