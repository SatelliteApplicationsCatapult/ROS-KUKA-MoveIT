#! /usr/bin/env python3
# Need to use python3 at the end!

# These are all addded in the dependencies initially (catkin_create_pkg <pkg_name> <dependencies>)
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rospy.init_node("move_turtle")

# pub = rospy.Publish('<topic name>', <msg type> queue_size=1)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

turtle_commands = Twist()

# Publishing at 2Hz
rate = rospy.Rate(1)

turtle_commands.linear.x = 2.0
turtle_commands.linear.y = 0
turtle_commands.linear.z = 0  # Don't change

turtle_commands.angular.x = 0  # Don't change
turtle_commands.angular.y = 0  # Don't change
turtle_commands.angular.z = -2.0


while not rospy.is_shutdown():
    
    # push the commans to the turtle to move it
    pub.publish(turtle_commands)    

    # Make the turtle sleep the required amount
    rate.sleep()