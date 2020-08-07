#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseArray.h>
#include <iostream> 
#include "ros/ros.h"
#include "std_msgs/Float32.h"
#include "geometry_msgs/TwistStamped.h"
#include "geometry_msgs/PoseStamped.h"
  
using namespace std;

geometry_msgs::PoseArray pos_connectors;
geometry_msgs::Pose goalpos;
float step = 0.005;
float anglestep = 1.0;

void posCallback(const geometry_msgs::PoseStamped::ConstPtr& msg)
{
  goalpos.position.x = msg->pose.position.x;
  goalpos.position.y = msg->pose.position.y;
  goalpos.position.z = msg->pose.position.z;
  goalpos.orientation.w = msg->pose.orientation.w;
  goalpos.orientation.x = msg->pose.orientation.x;
  goalpos.orientation.y = msg->pose.orientation.y;
  goalpos.orientation.z = msg->pose.orientation.z;
}

void stepCallback(const std_msgs::Float32::ConstPtr& msg)
{
  step = msg->data;
}

void anglestepCallback(const std_msgs::Float32::ConstPtr& msg)
{
  anglestep = msg->data;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "irb120_control");
  ros::NodeHandle node_handle;
  ros::Rate loop_rate(100);

  // ros::Subscriber vel_sub = node_handle.subscribe("/input/vel", 10, velCallback);
  ros::Subscriber pos_sub = node_handle.subscribe("/input/pos", 10, posCallback);
  ros::Subscriber step_sub = node_handle.subscribe("/input/step", 10, stepCallback);
  ros::Subscriber anglestep_sub = node_handle.subscribe("/input/anglestep", 10, anglestepCallback);
  
  
  moveit::planning_interface::MoveGroupInterface group("irb120");
  group.setPlanningTime(1);//0.1

  ros::AsyncSpinner spinner(10);
  spinner.start();

  geometry_msgs::Pose current_pose;
  current_pose = group.getCurrentPose().pose;
  goalpos = current_pose;

  group.setPoseTarget(goalpos);

  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  int key=0;
  std::cout << std::fixed;
  std::cout.precision(3);

  while(ros::ok())
  {
    // std::cout << "x: " << goalpos.position.x << "  y: " << goalpos.position.y << "  z: " << goalpos.position.z << "  yaw: " << atan2(2*(goalpos.orientation.w*goalpos.orientation.z + goalpos.orientation.x*goalpos.orientation.y), (1 - 2*(goalpos.orientation.y*goalpos.orientation.y + goalpos.orientation.z*goalpos.orientation.z)))/3.141592*180.0 -180.0<< "  pitch: " << asin(2*(goalpos.orientation.w*goalpos.orientation.y - goalpos.orientation.z*goalpos.orientation.x))/3.141592*180.0 << "  step: " << step <<"  anglestep: " << anglestep *2 <<std::endl;
    std::cout << "x: " << goalpos.position.x << "  y: " << goalpos.position.y << "  z: " << goalpos.position.z << "  w: " << goalpos.orientation.w << "  xa: " << goalpos.orientation.x << "  ya: " << goalpos.orientation.y << "  za: " << goalpos.orientation.z <<std::endl;

    group.setPoseTarget(goalpos);
    group.plan(my_plan);
    group.move();

    loop_rate.sleep();
    ros::spinOnce();
  }

  return 0;
}


