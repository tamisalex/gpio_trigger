#!/usr/bin/env python
# Author:

# pylint: disable=C0103

# Description

import sys
import rospy


# global variables
current_ = None


# callback functions
# ========================================
def cb_function(data):
    ''' does whatever your callback should do '''
    pass


# ========================================
def main_loop():
    ''' main loop '''
    rospy.init_node('test_node', anonymous=True)

    # publishers
    #pub = rospy.Publisher('topic_name', topic_type, queue_size=1)

    # subscribers
    # rospy.Subscriber('/topic_name', topic_type, cb_function)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        # main code
	print "Hello World"

        # publish updated list
        #pub.publish()
        rate.sleep()


# ============================
if __name__ == '__main__':
    try:
        main_loop()
    except rospy.ROSInterruptException:
        pass
