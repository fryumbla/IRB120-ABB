#!/usr/bin/env python
import rospy
import numpy as np
from keyboard.msg import Key
from geometry_msgs.msg import PoseStamped, Pose
from std_msgs.msg import Float32

class Key2Vel:

    def cable_callback(self, cable_msg):
        self.cable_pose.pose.position.x = 0.289 - cable_msg.position.y
        self.cable_pose.pose.position.y = -0.055 - cable_msg.position.x
        self.cable_pose.pose.position.z = 0.166
        self.cable_pose.pose.orientation.w = cable_msg.orientation.w
        self.cable_pose.pose.orientation.x = 0.0
        self.cable_pose.pose.orientation.y = 0.0
        self.cable_pose.pose.orientation.z = cable_msg.orientation.z

    def key_cb(self, key_msg):
        pos = PoseStamped()
        if key_msg.code == 119: #W, up
            self.desired_pose.pose.position.x = self.desired_pose.pose.position.x + self.step*np.cos(-self.yaw)
            self.desired_pose.pose.position.y = self.desired_pose.pose.position.y + self.step*np.sin(-self.yaw)
            print('up')

        elif key_msg.code== 281:    #PageDown, go to vision goal
            self.pitch = 0.0
            self.yaw = np.arcsin(self.cable_pose.pose.orientation.z)*2.0

            self.desired_pose.pose.position.x = self.cable_pose.pose.position.x
            self.desired_pose.pose.position.y = self.cable_pose.pose.position.y
            self.desired_pose.pose.position.z = self.cable_pose.pose.position.z

        elif key_msg.code== 280:    #PageUp, go to vision goal2
            self.pitch = 2.0 * np.pi / 180.0
            self.yaw = np.arcsin(self.cable_pose.pose.orientation.z)*2.0

            cablewidth = 0.015

            self.desired_pose.pose.position.x = self.cable_pose.pose.position.x - cablewidth*np.cos(-self.yaw)
            self.desired_pose.pose.position.y = self.cable_pose.pose.position.y - cablewidth*np.sin(-self.yaw)
            self.desired_pose.pose.position.z = 0.003

        elif key_msg.code == 115:   #S, down
            self.desired_pose.pose.position.x = self.desired_pose.pose.position.x - self.step*np.cos(-self.yaw)
            self.desired_pose.pose.position.y = self.desired_pose.pose.position.y - self.step*np.sin(-self.yaw)
            print('down')

        elif key_msg.code == 97:   #A, left
            self.desired_pose.pose.position.x = self.desired_pose.pose.position.x - self.step*np.sin(-self.yaw)
            self.desired_pose.pose.position.y = self.desired_pose.pose.position.y + self.step*np.cos(-self.yaw)
            print('left')

        elif key_msg.code == 100:   #D, right
            self.desired_pose.pose.position.x = self.desired_pose.pose.position.x + self.step*np.sin(-self.yaw)
            self.desired_pose.pose.position.y = self.desired_pose.pose.position.y - self.step*np.cos(-self.yaw)
            print('right')

        elif key_msg.code == 273:
            self.desired_pose.pose.position.z = self.desired_pose.pose.position.z + self.step

        elif key_msg.code == 274:
            if self.desired_pose.pose.position.z - self.step > 0.001:
                self.desired_pose.pose.position.z = self.desired_pose.pose.position.z - self.step
            else:
                self.desired_pose.pose.position.z = 0.001

        elif key_msg.code == 111: #O
            self.step = self.step + 0.001

        elif key_msg.code == 107: #K
            if self.step-0.001>0.001:
                self.step = self.step - 0.001
            else :
                self.step = 0.001

        elif key_msg.code == 112: #P
            self.anglestep = self.anglestep + 0.2

        elif key_msg.code == 108: #L
            if self.anglestep-0.2>0.2:
                self.anglestep = self.anglestep - 0.2
            else:
                self.anglestep = 0.2

        elif key_msg.code == 122: #Z
            self.pitch = self.pitch + self.anglestep/180.0*np.pi
        
        elif key_msg.code == 99: #C
            self.pitch = self.pitch - self.anglestep/180.0*np.pi

        
        elif key_msg.code == 113:   #Q, turn left
            self.yaw = self.yaw - self.anglestep/180.0*np.pi

        elif key_msg.code == 101:   #E, turn right
            self.yaw = self.yaw + self.anglestep/180.0*np.pi

        elif key_msg.code == 121 or key_msg.code == 49 :   #Y, 1 
            self.desired_pose.pose.position.x = 0.309085
            self.desired_pose.pose.position.y = 0.0
            # self.desired_pose.pose.position.z = 0.0010
            self.desired_pose.pose.position.z = 0.0040

            self.yaw = 0.0
            self.pitch = 6.0 * np.pi/180.0

        elif key_msg.code == 117 or key_msg.code == 51:   #U, 3
            # self.desired_pose.pose.position.x = 0.394
            self.desired_pose.pose.position.x = 0.384
            self.desired_pose.pose.position.y = 0.0
            # self.desired_pose.pose.position.z = 0.0010
            self.desired_pose.pose.position.z = 0.0030

            self.yaw = 0.0
            self.pitch = 6.0 * np.pi/180.0

        elif key_msg.code == 106 or key_msg.code == 55:   #J, 7
            self.desired_pose.pose.position.x = 0.309085
            self.desired_pose.pose.position.y = -0.100
            self.desired_pose.pose.position.z = 0.13607

            self.pitch = 0.0
            self.yaw = 0.0
            
        
        elif key_msg.code == 109 or key_msg.code == 56:   #M, 8
            self.desired_pose.pose.position.x = 0.309085
            self.desired_pose.pose.position.y = -0.107034
            self.desired_pose.pose.position.z = 0.13607

            self.pitch = 0.0
            self.yaw = 0.0

        elif key_msg.code == 44 or key_msg.code == 57:   #, 9
            self.desired_pose.pose.position.x = 0.259
            self.desired_pose.pose.position.y = 0.0
            self.desired_pose.pose.position.z = 0.13807

            self.pitch = 0.0
            self.yaw = 0.0

        elif key_msg.code == 278:   #Home, Camera recognition
            self.desired_pose.pose.position.x = 0.289
            self.desired_pose.pose.position.y = -0.055
            self.desired_pose.pose.position.z = 0.166

            self.pitch = 0.0
            self.yaw = 0.0

        elif key_msg.code == 104 or key_msg.code == 53:   #H, 5, stop
            self.desired_pose.pose.position.x = self.initial_pose.pose.position.x
            self.desired_pose.pose.position.y = self.initial_pose.pose.position.y
            self.desired_pose.pose.position.z = self.initial_pose.pose.position.z

            # self.desired_pose.pose.orientation.w = self.initial_pose.pose.orientation.w
            # self.desired_pose.pose.orientation.x = self.initial_pose.pose.orientation.x
            # self.desired_pose.pose.orientation.y = self.initial_pose.pose.orientation.y
            # self.desired_pose.pose.orientation.z = self.initial_pose.pose.orientation.z

            self.yaw = 0.0
            self.pitch = 0.0

        w_z = np.cos(self.yaw/2.0)
        x_z = 0.0
        y_z = 0.0
        z_z = np.sin(self.yaw/2.0)

        w_y = np.cos((self.pitch+np.pi)/2.0)
        x_y = 0.0
        y_y = np.sin((self.pitch+np.pi)/2.0)
        z_y = 0.0

        self.desired_pose.pose.orientation.w = w_y*w_z - x_y*x_z - y_y*y_z - z_y*z_z
        self.desired_pose.pose.orientation.x = w_y*x_z + x_y*w_z + y_y*z_z - z_y*y_z
        self.desired_pose.pose.orientation.y = w_y*y_z - x_y*z_z + y_y*w_z + z_y*x_z
        self.desired_pose.pose.orientation.z = w_y*z_z + x_y*y_z - y_y*x_z + z_y*w_z
        self.desired_pose.header.stamp = key_msg.header.stamp
        self.pos_pub.publish(self.desired_pose)
        self.step_pub.publish(self.step)
        self.anglestep_pub.publish(self.anglestep/2.0)


    def __init__(self):
        
        rospy.init_node('key2vel')
        self.r = rospy.Rate(10)
        self.pos_pub = rospy.Publisher('/input/pos', PoseStamped, queue_size=10)
        rospy.Subscriber('/keyboard/keydown', Key, self.key_cb)
        self.step_pub = rospy.Publisher('/input/step', Float32, queue_size=10)
        self.anglestep_pub = rospy.Publisher('/input/anglestep', Float32, queue_size=10)
        rospy.Subscriber('/cable/pose',Pose, self.cable_callback)

        self.initial_pose = PoseStamped()
        self.initial_pose.pose.position.x = 0.309085
        self.initial_pose.pose.position.y = 0.0
        self.initial_pose.pose.position.z = 0.13607
        self.initial_pose.pose.orientation.w = 0.0
        self.initial_pose.pose.orientation.x = 0.0
        self.initial_pose.pose.orientation.y = 1.0
        self.initial_pose.pose.orientation.z = 0.0
        
        self.step = 0.005
        self.anglestep = 2.0
        self.yaw = 0.0
        self.pitch = 0.0
        self.desired_pose = PoseStamped()
        self.desired_pose.pose.position.x = self.initial_pose.pose.position.x
        self.desired_pose.pose.position.y = self.initial_pose.pose.position.y
        self.desired_pose.pose.position.z = self.initial_pose.pose.position.z
        self.desired_pose.pose.orientation.w = self.initial_pose.pose.orientation.w
        self.desired_pose.pose.orientation.x = self.initial_pose.pose.orientation.x
        self.desired_pose.pose.orientation.y = self.initial_pose.pose.orientation.y
        self.desired_pose.pose.orientation.z = self.initial_pose.pose.orientation.z

        self.cable_pose = PoseStamped()
        self.cable_pose.pose.position.x = self.initial_pose.pose.position.x
        self.cable_pose.pose.position.y = self.initial_pose.pose.position.y
        self.cable_pose.pose.position.z = self.initial_pose.pose.position.z
        self.cable_pose.pose.orientation.w = self.initial_pose.pose.orientation.w
        self.cable_pose.pose.orientation.x = self.initial_pose.pose.orientation.x
        self.cable_pose.pose.orientation.y = self.initial_pose.pose.orientation.y
        self.cable_pose.pose.orientation.z = self.initial_pose.pose.orientation.z

    def loop(self):
        self.r.sleep()

if __name__ == '__main__':
    key2vel = Key2Vel()
    while not rospy.is_shutdown():
        key2vel.loop()