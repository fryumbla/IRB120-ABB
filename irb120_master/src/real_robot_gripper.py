#!/usr/bin/env python
import roslib;
import rospy
from sensor_msgs.msg import JointState

from trajectory_msgs.msg import JointTrajectory
from control_msgs.msg import FollowJointTrajectoryFeedback


class ABBandRobotiq3FGripperROSConnector:

    def __init__(self):
        
        self.robot_name = "ROBOTIQ-3F"

        # Initialize ROS node
        rospy.init_node('ABB_Robotiq_states')
        self.rate = rospy.Rate(20) # hz

        # Publish current robot state
        self.joint_state_pub = rospy.Publisher('joint_states', JointState, queue_size=10)
        # self.indy_state_pub = rospy.Publisher("/indy/status", GoalStatusArray, queue_size=10)
        self.control_state_pub = rospy.Publisher("/feedback_states", FollowJointTrajectoryFeedback, queue_size=1)

        # Subscribe desired joint position
        self.joint_execute_plan_sub = rospy.Subscriber("/ABB/joint_states", JointState, self.read_ABB_joint_states, queue_size=1)
        self.joint_execute_plan_sub = rospy.Subscriber("/Robotiq/joint_states", JointState, self.read_gripper3F_joint_states, queue_size=1)

        self.joint_execute_plan_sub = rospy.Subscriber("/ABB/feedback_states", FollowJointTrajectoryFeedback, self.read_ABB_feedback_states, queue_size=1)
        self.joint_execute_plan_sub = rospy.Subscriber("/Robotiq/feedback_states", FollowJointTrajectoryFeedback, self.read_gripper3F_feedback_states, queue_size=1)

        # # Subscribe desired joint position
        # self.joint_execute_plan_sub = rospy.Subscriber("/joint_path_command", JointTrajectory, self.execute_plan_result_cb, queue_size=1)

        # # Subscribe command
        # self.execute_joint_state_sub = rospy.Subscriber("/indy/execute_joint_state", JointState, self.execute_joint_state_cb, queue_size=1)
        # self.stop_sub = rospy.Subscriber("/stop_motion", Bool, self.stop_robot_cb, queue_size=1)
        # self.set_motion_param_sub = rospy.Subscriber("/indy/motion_parameter", Int32MultiArray, self.set_motion_param_cb, queue_size=1)

        # Misc variable


        self.ABB_joint_name_list = []
        self.ABB_joint_states_list = []

        self.gripper3F_joint_name_list = []
        self.gripper3F_joint_states_list = []

        self.ABB_feedback_states_list = []
        self.gripper3F_feedback_states_list = []
        # self.execute = False
        # self.vel = 3
        # self.blend = 5


    def __del__(self):
        self.indy.disconnect()

    def read_ABB_joint_states(self, msg):
        self.ABB_joint_name_list= msg.name
        self.ABB_joint_states_list = msg.position    

    def read_gripper3F_joint_states(self, msg):
        self.gripper3F_joint_name_list= msg.name
        self.gripper3F_joint_states_list = msg.position

    def read_ABB_feedback_states(self, msg):
        self.ABB_feedback_states_list = msg.actual.positions    

    def read_gripper3F_feedback_states(self, msg):
        self.gripper3F_feedback_states_list = msg.actual.positions
        


    def joint_state_publisher(self):
        
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = self.ABB_joint_name_list + self.gripper3F_joint_name_list
        joint_state_msg.position = list(self.ABB_joint_states_list) + list(self.gripper3F_joint_states_list)       
        joint_state_msg.velocity = []
        joint_state_msg.effort = []

        control_state_msg = FollowJointTrajectoryFeedback()
        control_state_msg.header.stamp = rospy.Time.now()
        control_state_msg.joint_names = self.ABB_joint_name_list + self.gripper3F_joint_name_list
        control_state_msg.actual.positions = list(self.ABB_feedback_states_list) + list(self.gripper3F_feedback_states_list) 
        control_state_msg.desired.positions = list(self.ABB_feedback_states_list) + list(self.gripper3F_feedback_states_list) 
        control_state_msg.error.positions = [0 for i in control_state_msg.joint_names]

        self.joint_state_pub.publish(joint_state_msg)
        self.control_state_pub.publish(control_state_msg)

    def run(self):

        while not rospy.is_shutdown():
            # self.current_robot_status = self.indy.get_robot_status()
            self.joint_state_publisher()
            # self.robot_state_publisher()

        # self.indy.disconnect()

def main():
    t = ABBandRobotiq3FGripperROSConnector()
    t.run()

if __name__ == '__main__':
    main()