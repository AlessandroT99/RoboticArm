# Robot Description

This ROS 2 package contains the URDF/Xacro description, configuration files, and launch scripts for a three-joint robotic arm. It is designed to integrate with the `ros2_control` framework for simulation and control purposes.

## Package Structure

- **`config/`**: Contains configuration files:
  - `simple_arm_controllers.yaml`: Configuration for the arm's controllers.
  - `urdf_setting.rviz`: RViz configuration file for visualization.

- **`gazebo/`**: Reserved for files related to Gazebo simulation.

- **`launch/`**: Contains launch scripts:
  - `robot_rviz.launch.py`: Launch file to visualize the robot in RViz.

- **`robots/`**: Contains robot description files:
  - `three_joints_arm.xacro`: Xacro file describing the robot's kinematics and geometry.

- **`ros2_control/`**: Placeholder for `ros2_control` configuration and setup.

- **`CMakeLists.txt` & `package.xml`**: Standard ROS 2 build and package configuration files.

## Features

- **Robot Description**: The robot's geometry and kinematics are defined using Xacro for modularity and reusability.
- **RViz Visualization**: Launch file and configuration for visualizing the robot in RViz.
- **Controller Integration**: Example configuration for `ros2_control` to manage the robot's actuators and joints (to be developed).


## Dependencies

This package depends on the following ROS 2 packages:
- `ros2_control`
- `robot_state_publisher`
- `rviz2`

Make sure to install these dependencies before using the package.

### Install Dependencies
To install the dependencies for a generic ROS 2 version, use the following commands:
```bash
sudo apt update
sudo apt install ros-$ROS-DISTRO-robot-state-publisher
sudo apt install ros-$ROS-DISTRO-ros2-control
sudo apt install ros-$ROS-DISTRO-rviz2
```
`$ROS-DISTRO` will be automatically replaced with your ROS 2 distribution (e.g., `humble`, `foxy`, `rolling`). In this project we are using the [`jazzy`](https://docs.ros.org/en/jazzy/index.html) version.

## Usage

### 1. Launch RViz Visualization
To visualize the robot in RViz, use the following command:
```bash
ros2 launch robot_description robot_rviz.launch.py
```

### 3. Extend the Description
The robot's description can be modified or extended by editing the `robots/three_joints_arm.xacro` file. Refer to the [URDF documentation](https://wiki.ros.org/urdf) and [Xacro documentation](https://wiki.ros.org/xacro) for syntax and examples.

## References

- [ROS 2 Documentation](https://docs.ros.org/)
- [ros2_control Framework](https://control.ros.org/)
