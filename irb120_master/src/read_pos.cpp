#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseArray.h>
#include <iostream> 
  
using namespace std;

geometry_msgs::PoseArray pos_connectors;

int main(int argc, char **argv)
{
  ros::init(argc, argv, "irb120_control");
  ros::NodeHandle node_handle;  
  ros::AsyncSpinner spinner(1);
  spinner.start();
  
  moveit::planning_interface::MoveGroupInterface group("irb120");
  group.setPlanningTime(1);//0.1

  // start programing

  geometry_msgs::Pose current_pose;
  current_pose = group.getCurrentPose().pose;
  std::cout << std::endl << "CUrrent Pose End Effector" << std::endl;
  std::cout << "X: " << current_pose.position.x << std::endl;
  std::cout << "Y: " << current_pose.position.y << std::endl;
  std::cout << "Z: " << current_pose.position.z << std::endl;
  std::cout << "w: " << current_pose.orientation.w << std::endl;
  std::cout << "x: " << current_pose.orientation.x << std::endl;
  std::cout << "y: " << current_pose.orientation.y << std::endl;
  std::cout << "z: " << current_pose.orientation.z << std::endl;

  return 0;
}


