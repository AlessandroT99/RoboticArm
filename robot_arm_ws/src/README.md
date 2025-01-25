## Package Overview

### 1. **`controllers_pkg`**
This package is dedicated to developing custom controllers for the robotic arm. It includes the logic and algorithms necessary to control the arm's movements.

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
    │   └── cpp_package_name  
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