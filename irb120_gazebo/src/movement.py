#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def main():
    

    rospy.init_node("stand_up")

    while not rospy.is_shutdown():
        
        number = input ("Enter number: ")
        if (number==1):
            joint_position_state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if (number==2):
            print("dos")
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0,0,0,0,0,0,0,0,0,0,0,0,-0.5]
        if (number==3):
            #parado
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0.5]
        if (number==4):
            #derecha alza
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0,0,0,0,0,0,0,0,0,0,0,0.3,0.5]		
        if (number==5):
            # primer paso
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0,0,0,0,0,0,0,0,0,0,0,-0.3,0]
        if (number==6):
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0.3,0,0,0,0,0,0,0,0,0,0,0,0]	
        if (number==7):
            # segundo paso
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if (number==8):
            # segundo paso
            joint_position_state=[0.5,-0.5,0.5,-0.5,0.5,-0.5,-0.5,0.5,0,-0.3,0,0,0,0,0,0,0,0,0,0,0]
        if (number==9):
            # segundo paso
            joint_position_state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    
        pub = rospy.Publisher('joint_states', JointState, queue_size=10)
        # rate = rospy.Rate(1000000) # 10hz
        joints_states = JointState()
        joints_states.header = Header()
        joints_states.header.stamp = rospy.Time.now()
        joints_states.name = ["joint_1","joint_2","joint_3","joint_4","joint_5","joint_6","joint_7","joint_8","joint_9","joint_10","joint_11","joint_12","joint_13","joint_14","joint_15","joint_16","joint_17","joint_18","joint_19","joint_20","joint_21"]
        joints_states.position = joint_position_state
        pub.publish(joints_states)
        rate = rospy.Rate(10) # 10hz   
        # rospy.sleep(5)

if __name__ == '__main__':
    main()