import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution, Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    pkg_ros_gz_sim = FindPackageShare(package='ros_gz_sim').find('ros_gz_sim')
    pkg_share_gazebo = FindPackageShare(package='robot_gazebo').find('robot_gazebo')
    pkg_share_description = FindPackageShare(package='robot_description').find('robot_description')

    world_path = PathJoinSubstitution([pkg_share_gazebo,'world','basic_world.sdf'])
    
    default_model_path = PathJoinSubstitution([pkg_share_description, 'robots', 'arm.urdf.xacro'])
    robot_description_config = Command(['xacro ', default_model_path])


    #-------------------------------------------------------------    
    robot_state_publisher_node = Node(package='robot_state_publisher',
                                      executable='robot_state_publisher',
                                      parameters=[
                                          {'robot_description': robot_description_config}])

    gz_sim_launch_file = os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')

    start_gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gz_sim_launch_file),
        launch_arguments={
            'gz_args': [' -r -v 4 ', world_path], 
            'on_exit_shutdown': 'true'}
            .items())
    
    start_gazebo_ros_spawner_cmd = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-topic', '/robot_description',
            '-name', 'simple_robot_arm',
            '-allow_renaming', 'true'])

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller", "--controller-manager", "/controller_manager"],
    )
    
    start_gazebo_ros_bridge_cmd = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_share_gazebo, 'config', 'ros_gz_bridge.yaml'),
        }],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(DeclareLaunchArgument(name='model', default_value=default_model_path,
                                        description='Path to robot urdf file relative to urdf_tutorial package'))
    ld.add_action(robot_state_publisher_node)
    ld.add_action(start_gazebo_cmd)
    ld.add_action(start_gazebo_ros_bridge_cmd)
    ld.add_action(start_gazebo_ros_spawner_cmd)
    ld.add_action(arm_controller_spawner)
    ld.add_action(joint_state_broadcaster_spawner)
    return ld