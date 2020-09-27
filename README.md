[![ROS](http://www.ros.org/wp-content/uploads/2013/10/rosorg-logo1.png)](http://www.ros.org/)

<h1 style="border:none"> RISE ABB IRB-120 ROS Manipulation Package </h1>
&copy; 2020, Francisco Yumbla

<hr>

## 1. How to Install

### 1.1. System Requirements

This package is written an tested on **Ubuntu 18.04 + ROS Melodic** environment. Dependencies are also for this environment.

Note: the same package can work in **Ubuntu 16.04 + ROS Kinetic**

### 1.2. Dependencies Prerequisites

There are a number of dependencies in this package, since the ABB robot is operated by ROS-Industrial package. Please install all the packages listed below in your Ubuntu PC, in the given order. These packages can be installed by `apt` package manager.

* ros-melodic-desktop-full
* ros-melodic-industrial-core
* ros-melodic-industrial-msgs
* ros-melodic-industrial-robot-client
* ros-melodic-industrial-robot-simulator
* ros-melodic-industrial-utils
* ros-melodic-abb
* ros-melodic-moveit
* ros-melodic-joint-state-publisher-gui
* ros-melodic-joint-trajectory-controller

Now,Extract the metapackage `IRB120-ABB` into `${ros_workspace}/src`. `catkin_make` your workspace.

**WARNING: If you planing use grippers with this robot. You need copy the gripper package https://github.com/fryumbla/Robotiq-grippers.git**

*If you want control with the joystick control. You need install: `sudo pip install ds4drv`


## 2. Structure of Packages

* **irb120_description:** This package contains the URDF and XACRO friles for diferents configuration of the robot with grippers.
* **irb120_master:** This pasckage contains a diferrents examples of motion used MoveIt and the joystick&keyboard control of the real robot.
* **irb120_vrep:** This package contains the communication with V-REP simulator including examples and scenes
* **irb120_configuration_moveit:** This package contains the diferent MoveIt configuration of diferents configuration of the robot

## 3. How to Use

### 3.1. Simulation

Open terminal and `roscore` and `Enter`. 

#### 3.1.1 Rviz Visualization

1. Launch the robot visualization Rviz
   ```
   roslaunch irb120_description irb120_display.launch
   ```
   If you need see other configuration you can space and include **gripper_2f:=true** or **gripper_3f:=true**
   ```
   roslaunch irb120_description irb120_display.launch gripper_2f:=true
   ```

2. Launch the robot with Moveit configuration
   ```
   roslaunch irb120_description irb120_moveit.launch
   ```
   If you need see other configuration you can space and include **gripper_2f:=true** or **gripper_3f:=true**
   ```
   roslaunch irb120_description irb120_moveit.launch gripper_3f:=true
   ```

#### 3.1.2 V-REP Simulation

1. V-REP execution (Since simulation is performed with vrep remote api and PLAY, roscore must be executed first): Open the scene of the irb120_vrep/scenes folder 


2. Run the step 3.1.1 visualization Rviz or MoveIt

3. Run the next node for the communication Vrep to ros
   ```
   rosrun irb120_vrep comunication
   ```
4. You can control with publish direct the Jointstates or generate other but you need change the subscribe in the **vrep_control.cpp** file

You can find a example to publish a new joint mesage:

To see the list of movement, type `rosrun irb120_vrep movement.py` program, introduce the number do you want to move `1 2 3 4 5` and `Enter`.
This node publish the joints goals in the topic `/joint_goals` or the joints states in the topic `/joint_states`

#### 3.1.2 Gazebo Simulation (in construction)

1. Launch the robot in gazebo
   ```
   roslaunch irb120_gazebo gazebo.launch

   ```

2. Run the next node for the communication ROS to Gazebo
   ```
   rosrun irb120_gazebo communitation_gazebo.py 
   ```
To see the list of movement, type `rosrun bioloid_gp_master movement.py` program, introduce the number do you want to move `1 2 3` and `Enter`.
This node publis the joints goals in the topic `/joint_goals`

### 3.2. Real Robot

The real robot work with the moveit_configuration package for precaution collission in our workspace or enviroment

Setup the Robot and turn on. 

2. Launch the robot
   ```
   roslaunch irb120_description real_robot.launch robot:=true
   ```
   If you need see other configuration you change robot:=true for **gripper_2f:=true** or **gripper_3f:=true**
   ```
   roslaunch irb120_description real_robot.launch gripper_2f:=true
   ```

<!-- moveit

    para crear uno nuevo moveit se debe anadir 
    config folder
    joint_names.yaml
    
    se debe copiar moveit_planing_execution.launch  cambiando con la carpeta moveit correspondiente

    se debe cambiar en 
    ros_controlllers.yaml

    controller_list:
  - name: irb_120_controller
    action_ns: follow_joint_trajectory
    default: True
    type: FollowJointTrajectory
    joints:
      - joint_1
      - joint_2
      - joint_3
      - joint_4
      - joint_5
      - joint_6

    por

    controller_list:
  - name: ""
    action_ns: joint_trajectory_action
    default: True
    type: FollowJointTrajectory
    joints:
      - joint_1
      - joint_2
      - joint_3
      - joint_4
      - joint_5
      - joint_6
