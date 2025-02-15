## Package Overview

### 2. **`robot_description`**
This package contains the robot's URDF/Xacro description, RViz configurations, and controller settings. 

### 3. **`robot_gazebo`**
This package is used to simulate the robotic arm in Gazebo, providing a testing environment for controllers and algorithms.

## Add a new package
Following the instruction to add a new package in this workspace. Considering that the workspace has already been created (follow the [ROS documentation](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)), let's open a terminal, and make sure you are in the `src` folder of your workspace before running the package creation command.
```bash
cd ~/your_workspace_name/src
```
The command syntax for creating a new package in ROS 2 is:
```bash
ros2 pkg create cpp_package_name --build-type ament_cmake --dependencies rclcpp
```
The architecture of your new C++ package will look like this:
```		
/home/ubuntu_name/your_workspace_name/src/cpp_package_name/

    ├── CMakeLists.txt  
    ├── include  
    │   └── cpp_package_name  
    ├── package.xml  
    └── src
```
Now, to build this package you need to add it to the **CMakeLists.txt** file using the following syntax (see the one in the repo as an example):
```
add_subdirectory(cpp_package_name)
```
Then, move to the workspace folder with `cd ~/your_workspace_name`, and from here build the package you just created with
```bash
colcon build
```
or 

```bash
colcon build --packages-select cpp_package_name
```
to build a specific package.


## Rum the simulation

Execute the following command in a single terminal, and make sure to have the most updated version of the branch.
```bash

cd ~/path_to_your_workspace/robot_arm_ws

colcon build

ros2 launch robot_gazebo gazebo_sim.launch.py

```
In my case it will be 
```bash

cd ~/Documents/RoboticArm/robot_arm_ws

colcon build

ros2 launch robot_gazebo gazebo_sim.launch.py

```

Once the simulation is running, up to now the only way to move the robot is using command in the terminal. So open a new terminal and use to following command to set the new goal positions of all the joints:
```bash
ros2 topic pub --once /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{joint_names: ['joint1', 'joint2', 'joint3'], points: [{positions: [x.x, x.x, x.x], time_from_start: {sec: 3.0}}]}"
```
Change the **x.x** with the value that you want.