#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState

from std_msgs.msg import Header
from std_msgs.msg import Float64

# global joint_goals


joint_goals = JointState()
joint_goals.position = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

def callback(data):
	joint_goals.header = Header()
	joint_goals.header.stamp = rospy.Time.now()
	joint_goals.name = data.name
	joint_goals.position = data.position
	

def main():

	rospy.init_node("communication_gazebo")

	pub1 = rospy.Publisher('bioloidgp_social_robot/joint1_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('bioloidgp_social_robot/joint2_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('bioloidgp_social_robot/joint3_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('bioloidgp_social_robot/joint4_position_controller/command', Float64, queue_size=10)
	pub5 = rospy.Publisher('bioloidgp_social_robot/joint5_position_controller/command', Float64, queue_size=10)
	pub6 = rospy.Publisher('bioloidgp_social_robot/joint6_position_controller/command', Float64, queue_size=10)
	pub7 = rospy.Publisher('bioloidgp_social_robot/joint7_position_controller/command', Float64, queue_size=10)
	pub8 = rospy.Publisher('bioloidgp_social_robot/joint8_position_controller/command', Float64, queue_size=10)
	pub9 = rospy.Publisher('bioloidgp_social_robot/joint9_position_controller/command', Float64, queue_size=10)
	pub10 = rospy.Publisher('bioloidgp_social_robot/joint10_position_controller/command', Float64, queue_size=10)
	pub11 = rospy.Publisher('bioloidgp_social_robot/joint11_position_controller/command', Float64, queue_size=10)
	pub12 = rospy.Publisher('bioloidgp_social_robot/joint12_position_controller/command', Float64, queue_size=10)
	pub13 = rospy.Publisher('bioloidgp_social_robot/joint13_position_controller/command', Float64, queue_size=10)
	pub14 = rospy.Publisher('bioloidgp_social_robot/joint14_position_controller/command', Float64, queue_size=10)
	pub15 = rospy.Publisher('bioloidgp_social_robot/joint15_position_controller/command', Float64, queue_size=10)
	pub16 = rospy.Publisher('bioloidgp_social_robot/joint16_position_controller/command', Float64, queue_size=10)
	pub17 = rospy.Publisher('bioloidgp_social_robot/joint17_position_controller/command', Float64, queue_size=10)
	pub18 = rospy.Publisher('bioloidgp_social_robot/joint18_position_controller/command', Float64, queue_size=10)
	pub19 = rospy.Publisher('bioloidgp_social_robot/joint19_position_controller/command', Float64, queue_size=10)
	pub20 = rospy.Publisher('bioloidgp_social_robot/joint20_position_controller/command', Float64, queue_size=10)
	pub21 = rospy.Publisher('bioloidgp_social_robot/joint21_position_controller/command', Float64, queue_size=10)

	# rospy.Subscriber('joint_goals', JointState, callback)
	
	while not rospy.is_shutdown():
		rospy.Subscriber('joint_goals', JointState, callback)
		pub1.publish(joint_goals.position[0])
		pub2.publish(joint_goals.position[1])
		pub3.publish(joint_goals.position[2])
		pub4.publish(joint_goals.position[3])
		pub5.publish(joint_goals.position[4])
		pub6.publish(joint_goals.position[5])
		pub7.publish(joint_goals.position[6])
		pub8.publish(joint_goals.position[7])
		pub9.publish(joint_goals.position[8])
		pub10.publish(joint_goals.position[9])
		pub11.publish(joint_goals.position[10])
		pub12.publish(joint_goals.position[11])
		pub13.publish(joint_goals.position[12])
		pub14.publish(joint_goals.position[13])
		pub15.publish(joint_goals.position[14])
		pub16.publish(joint_goals.position[15])
		pub17.publish(joint_goals.position[16])
		pub18.publish(joint_goals.position[17])
		pub19.publish(joint_goals.position[18])
		pub20.publish(joint_goals.position[19])
		pub21.publish(joint_goals.position[20])
		rate = rospy.Rate(10)
		

if __name__ == '__main__':
	main()