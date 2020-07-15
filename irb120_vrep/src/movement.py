#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState
from std_msgs.msg import Header


def main():
    

    rospy.init_node("stand_up")

    while not rospy.is_shutdown():
        
        number = input ("Enter number: ")
        if (number==1):
            joint_position_state=[0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        if (number==2):
            joint_position_state=[0.80, 0.50, 0, 0.5, 1, 0.0, 0.8, 0.8, -0.8, 0.8, 0.8, -0.8]
        if (number==3):
            #parado
            joint_position_state=[0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.8, 0.8, -0.8, 0.8, 0.8, -0.8]
        if (number==4):
            #derecha alza
            joint_position_state=[0.0, 0.5, 0, 0.5, 0.0, 0.5, 0.8, 0.8, -0.8, 0.8, 0.8, -0.8]		
        if (number==5):
            # primer paso
            joint_position_state=[0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.8, 0.8, -0.8, 0.8, 0.8, -0.8]

        pub = rospy.Publisher('joint_states', JointState, queue_size=10)
        # rate = rospy.Rate(1000000) # 10hz
        joints_states = JointState()
        joints_states.header = Header()
        joints_states.header.stamp = rospy.Time.now()
        joints_states.name = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "finger_joint", "left_inner_knuckle_joint","left_inner_finger_joint", "right_outer_knuckle_joint", "right_inner_knuckle_joint", "right_inner_finger_joint"]
        joints_states.position = joint_position_state
        pub.publish(joints_states)
        rate = rospy.Rate(10) # 10hz   
        # rospy.sleep(5)

if __name__ == '__main__':
    main()