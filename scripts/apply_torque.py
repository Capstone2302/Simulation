#!/usr/bin/env python3

import rospy
from gazebo_msgs.srv import ApplyJointEffort
from std_msgs.msg import Float64

# Set the name of the joint to apply the effort to
JOINT_NAME = "revolute"

def apply_torque(torque):
    # Create a publisher to send the effort command
    effort_pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=1)
    rospy.init_node('apply_joint_effort_node')

    # Create an ApplyJointEffort message
    effort_msg = ApplyJointEffort()
    effort_msg.joint_name = JOINT_NAME
    effort_msg.effort = torque

    # Set the start time of the effort command
    effort_msg.start_time = rospy.Time.now()

    # Set the duration of the effort command
    duration = rospy.Duration.from_sec(1.0)
    effort_msg.duration = duration

    # Publish the effort command
    effort_pub.publish(effort_msg)

if __name__ == '__main__':
    # Wait for the simulation to start up
    rospy.sleep(5)

    # Apply a torque of 1 Nm to the joint
    apply_torque(1.0)

