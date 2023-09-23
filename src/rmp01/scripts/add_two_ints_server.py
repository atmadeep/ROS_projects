#!/usr/bin/env python

for rmp01.srv import AddTwoInts, AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print(f"Returning sum of {req.a} {req.b}")
    return 