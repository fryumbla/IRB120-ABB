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

  // We can print the name of the reference frame for this robot.
  ROS_INFO("Reference frame: %s", group.getPlanningFrame().c_str());
  
  // We can also print the name of the end-effector link for this group.
  ROS_INFO("Reference frame: %s", group.getEndEffectorLink().c_str());

    geometry_msgs::Pose goalpos;
  
    goalpos.position.x = 0.30202;
    goalpos.position.y = 0;
    goalpos.position.z = 0.318022; // this is z go down put 0
    goalpos.orientation.w = 0;
    goalpos.orientation.x = 0;
    goalpos.orientation.y = 1;
    goalpos.orientation.z = 0;
    group.setPoseTarget(goalpos);

    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    moveit::planning_interface::MoveItErrorCode success = group.plan(my_plan); 
    ROS_INFO("Visualizing plan 1 (pose goal) %s",success.val ? "":"FAILED"); 
    // group.execute(my_plan);
    group.move();

    sleep(2.0);

    // goalpos.position.y = 0.0001; // this is z go down put 0
    goalpos.position.z = 0.0001; // this is z go down put 0

    group.setPoseTarget(goalpos);
    moveit::planning_interface::MoveGroupInterface::Plan my_plan1;
    moveit::planning_interface::MoveItErrorCode success1 = group.plan(my_plan1); 
    ROS_INFO("Visualizing plan 1 (pose goal) %s",success1.val ? "":"FAILED"); 
    group.move();
    sleep(2.0);
  
  // sleep(10.0);

  // ros::waitForShutdown();
  // ros::spin();

  return 0;
}


