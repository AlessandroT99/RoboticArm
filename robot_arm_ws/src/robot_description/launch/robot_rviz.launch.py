import os
import xacro
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command

def generate_launch_description():

    """
    Automatically open rviz2 and visualize the robot described in the URDF file.\n
    This file name and path has to be set inside the code.

    You can use this to test quickly you URDF file and see if it is correct
    """

    pkg_default_path = FindPackageShare('robot_description')
    rviz_config_file_path = PathJoinSubstitution([pkg_default_path, 'config', 'urdf_setting.rviz'])
    default_model_path = PathJoinSubstitution([pkg_default_path, 'robots', 'arm.urdf.xacro'])

    # Declare of arguments
    # gui_arg = DeclareLaunchArgument(name='gui', default_value='true',
    #                                 description='Flag to enable joint_state_publisher_gui')
    
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=rviz_config_file_path,
                                     description='Absolute path to rviz config file')
    
    # Process of the Xacro file to get the URDF file
    robot_description_config = Command(['xacro ', default_model_path])
    
    
    # Robot state publisher is a mandatory node to convert the joint states into a 3D pose of the robot,
    # based on the robot model defined in the URDF file.
    robot_state_publisher_node = Node(package='robot_state_publisher',
                                      executable='robot_state_publisher',
                                      parameters=[{
                                          'robot_description': robot_description_config}])
    
    joint_state_pub_gui = Node(package='joint_state_publisher_gui',
                               executable='joint_state_publisher_gui')
    
    rviz2_node = Node(package='rviz2',
                      executable='rviz2',
                      output='screen',
                      arguments=['-d', LaunchConfiguration('rvizconfig')])


    ld = LaunchDescription()

    # Arguments
    # ld.add_action(gui_arg)
    ld.add_action(rviz_arg)

    # Nodes
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_pub_gui)
    ld.add_action(rviz2_node)

    return ld