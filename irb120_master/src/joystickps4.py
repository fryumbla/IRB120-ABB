#!/usr/bin/env python
import rospy
import numpy as np
import moveit_commander
import moveit_msgs.msg
from ds4_driver.msg import Status
from geometry_msgs.msg import PoseStamped, Pose
from std_msgs.msg import Float32

class Key2Vel:

    def key_cb(self, key_msg):
        pos = PoseStamped()
        if key_msg.button_dpad_up == 1: #W, X UP
            self.desired_pose.pose.position.x = self.desired_pose.pose.position.x + self.step
            # self.desired_pose.pose.position.y = self.desired_pose.pose.position.y + self.step
            print('up')

        elif key_msg.button_dpad_down == 1:   #S, X DOWN
            self.desired_pose.pose.position.x = self.desired_pose.pose.position.x - self.step
            # self.desired_pose.pose.position.y = self.desired_pose.pose.position.y - self.step
            print('down')

        elif key_msg.button_dpad_left == 1:   #A, left
            # self.desired_pose.pose.position.x = self.desired_pose.pose.position.x - self.step
            self.desired_pose.pose.position.y = self.desired_pose.pose.position.y + self.step
            print('left')

        elif key_msg.button_dpad_right == 1:   #D, right
            # self.desired_pose.pose.position.x = self.desired_pose.pose.position.x + self.step
            self.desired_pose.pose.position.y = self.desired_pose.pose.position.y - self.step
            print('right')

        elif key_msg.button_triangle == 1:   #KEY_UP
            self.desired_pose.pose.position.z = self.desired_pose.pose.position.z + self.step

        elif key_msg.button_cross == 1:   #KEY_DOWN
            if self.desired_pose.pose.position.z - self.step > 0.001:
                self.desired_pose.pose.position.z = self.desired_pose.pose.position.z - self.step
            else:
                self.desired_pose.pose.position.z = 0.001

        elif key_msg.button_ps == 1:   #HOME_POS
            self.desired_pose.pose.position.x = self.initial_pose.pose.position.x
            self.desired_pose.pose.position.y = self.initial_pose.pose.position.y
            self.desired_pose.pose.position.z = self.initial_pose.pose.position.z
            self.desired_pose.pose.orientation.w = self.initial_pose.pose.orientation.w
            self.desired_pose.pose.orientation.x = self.initial_pose.pose.orientation.x
            self.desired_pose.pose.orientation.y = self.initial_pose.pose.orientation.y
            self.desired_pose.pose.orientation.z = self.initial_pose.pose.orientation.z

        # w_z = np.cos(self.yaw/2.0)
        # x_z = 0.0
        # y_z = 0.0
        # z_z = np.sin(self.yaw/2.0)

        # w_y = np.cos((self.pitch+np.pi)/2.0)
        # x_y = 0.0
        # y_y = np.sin((self.pitch+np.pi)/2.0)
        # z_y = 0.0

        # self.desired_pose.pose.orientation.w = w_y*w_z - x_y*x_z - y_y*y_z - z_y*z_z
        # self.desired_pose.pose.orientation.x = w_y*x_z + x_y*w_z + y_y*z_z - z_y*y_z
        # self.desired_pose.pose.orientation.y = w_y*y_z - x_y*z_z + y_y*w_z + z_y*x_z
        # self.desired_pose.pose.orientation.z = w_y*z_z + x_y*y_z - y_y*x_z + z_y*w_z

        self.desired_pose.header.stamp = key_msg.imu.header.stamp
        self.pos_pub.publish(self.desired_pose)
        # self.step_pub.publish(self.step)
        # self.anglestep_pub.publish(self.anglestep/2.0)


    def __init__(self):

        rospy.init_node('joystick')
        self.r = rospy.Rate(10)
        self.pos_pub = rospy.Publisher('/input/pos', PoseStamped, queue_size=10)
        rospy.Subscriber('/status', Status, self.key_cb)
        self.step_pub = rospy.Publisher('/input/step', Float32, queue_size=10)
        self.anglestep_pub = rospy.Publisher('/input/anglestep', Float32, queue_size=10)
        # rospy.Subscriber('/cable/pose',Pose, self.cable_callback)

        self.group = moveit_commander.MoveGroupCommander("irb120")
        self.current_pos = self.group.get_current_pose()

        self.initial_pose = PoseStamped()
        self.initial_pose = self.current_pos
      
        self.step = 0.001
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