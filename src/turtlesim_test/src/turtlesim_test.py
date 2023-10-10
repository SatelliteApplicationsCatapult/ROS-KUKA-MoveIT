#! /usr/bin/env python3
# Need to use python3 at the end!

# These are all addded in the dependencies initially (catkin_create_pkg <pkg_name> <dependencies>)
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from time import sleep

# function to show the node value as it moves
def callback(variable):
    print("\nData Point\n",variable)
    # sleep(0.5)
    # Currently filling screen, know that it works
    # pass

# starting the node that will listen to and publish from
rospy.init_node("listen_turtle")

# sub = rospy.Subscriber('<topic_name>', <msg_type>, <func_name>)
# listens to the topic and calls the callback function everytime it hears something - does not need a loop
sub = rospy.Subscriber('/turtle1/pose', Pose, callback)

rospy.spin()




