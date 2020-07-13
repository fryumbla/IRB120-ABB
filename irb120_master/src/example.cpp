#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseArray.h>
#include <iostream> 
  
using namespace std;

geometry_msgs::PoseArray pos_connectors;

void chatterCallback(const geometry_msgs::PoseArray& msg)
{
    
  pos_connectors= msg;



  // sleep(2.0);

  // geometry_msgs::Pose current_pose;
  // current_pose = group.getCurrentPose().pose;
  // std::cout << current_pose.position.x << std::endl;
  // std::cout << current_pose.position.y << std::endl;
  // std::cout << current_pose.position.z << std::endl;
  // std::cout << current_pose.orientation.w << std::endl;
  // std::cout << current_pose.orientation.x << std::endl;
  // std::cout << current_pose.orientation.y << std::endl;
  // std::cout << current_pose.orientation.z << std::endl;




  
  
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "grasping_connectors");
  ros::NodeHandle node_handle;  
  ros::AsyncSpinner spinner(2);
  spinner.start();
  
  ros::Subscriber sub = node_handle.subscribe("/connector/position_connector", 1000, chatterCallback);
  // ros::waitForShutdown();

  moveit::planning_interface::MoveGroupInterface group("indy7");
  group.setPlanningTime(1);//0.1
  // We can print the name of the reference frame for this robot.
  ROS_INFO("Reference frame: %s", group.getPlanningFrame().c_str());
  
  // We can also print the name of the end-effector link for this group.
  ROS_INFO("Reference frame: %s", group.getEndEffectorLink().c_str());

  std::cout << "dimension: " << pos_connectors.poses.size() << std::endl;

  for (int i = 0; i < pos_connectors.poses.size(); i++)
  {
    geometry_msgs::Pose home_camera;
  
    home_camera.position.x = 0.4;
    home_camera.position.y = -0.03;
    home_camera.position.z = 0.75;
    // 0.18 cerca de la mesa y 0.20 seria el fijo 
    home_camera.orientation.w = 0;
    home_camera.orientation.x = -0.7071068;
    home_camera.orientation.y = 0.7071068;
    home_camera.orientation.z = 0;
    group.setPoseTarget(home_camera);

    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    moveit::planning_interface::MoveItErrorCode success = group.plan(my_plan); 
    ROS_INFO("Visualizing plan 1 (pose goal) %s",success.val ? "":"FAILED"); 
    // group.execute(my_plan);
    group.move();

    sleep(3.0);

    std::cout << "Connector " << i << std::endl;
    geometry_msgs::Pose goal;  
    std::cout << "x,y " << pos_connectors.poses.at(i).position.x << "," << pos_connectors.poses.at(i).position.y << std::endl;
    goal.position.x = pos_connectors.poses.at(i).position.x+0.4+0.063;
    goal.position.y = pos_connectors.poses.at(i).position.y-0.03+0.03;
    goal.position.z = 0.20;
    // 0.18 cerca de la mesa y 0.20 seria el fijo 
    goal.orientation.w = 0;
    goal.orientation.x = -0.7071068;
    goal.orientation.y = 0.7071068;
    goal.orientation.z = 0;

    group.setPoseTarget(goal);
    moveit::planning_interface::MoveGroupInterface::Plan my_plan1;
    moveit::planning_interface::MoveItErrorCode success1 = group.plan(my_plan1); 
    ROS_INFO("Visualizing plan 1 (pose goal) %s",success1.val ? "":"FAILED"); 
    group.move();
    sleep(3.0);
    
  }

  // sleep(10.0);

  // ros::waitForShutdown();
  // ros::spin();

  return 0;
}







// class MoveEnable{
// public:
//     void coordsCallback(const geometry_msgs::PoseArray waypoints);
// };

// void MoveEnable::coordsCallback(const geometry_msgs::PoseArray waypoints){

//   geometry_msgs::PoseArray pos_connectors= waypoints;
  

//   geometry_msgs::Pose home_camera;
  
//   home_camera.position.x = 0.4;
//   home_camera.position.y = -0.03;
//   home_camera.position.z = 0.75;
//   // 0.18 cerca de la mesa y 0.20 seria el fijo 
//   home_camera.orientation.w = 0;
//   home_camera.orientation.x = -0.7071068;
//   home_camera.orientation.y = 0.7071068;
//   home_camera.orientation.z = 0;

//   moveit::planning_interface::MoveGroupInterface move_group("indy7");
  
//   // We can print the name of the reference frame for this robot.
//   ROS_INFO("Reference frame: %s", move_group.getPlanningFrame().c_str());
  
//   // We can also print the name of the end-effector link for this group.
//   ROS_INFO("Reference frame: %s", move_group.getEndEffectorLink().c_str());
//   ROS_INFO("hola");
//   move_group.setPoseTarget(home_camera);

//   moveit::planning_interface::MoveGroupInterface::Plan my_plan;
//   moveit::planning_interface::MoveItErrorCode success = move_group.plan(my_plan); 
//   ROS_INFO("Visualizing plan 1 (pose goal) %s",success.val ? "":"FAILED"); 
//   move_group.execute(my_plan);

//   sleep(5);


// }

// int main(int argc, char** argv)
// {

//   ros::init(argc, argv, "grasping_connectors");
//   ros::NodeHandle nh;
//   // ros::AsyncSpinner spinner(2);
//   // spinner.start();

//   MoveEnable mv;

//   ros::Subscriber sub = nh.subscribe("/connector/position_connector", 1000, &MoveEnable::coordsCallback, &mv);

//   ros::spin();

//   // ros::waitForShutdown();
//   return 0;
//  }