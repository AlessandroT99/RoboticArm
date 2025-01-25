# robot_gazebo package description
This folder contains all the setup files required to run the simulation of a three joints robotic arm on Gazebo. The Gazebo version used in this project: 8.7.0

## /world folder
In Gazebo, a world is essentially a simulation environment that defines everything within it, including the 3D models, terrain, physics properties, lighting, sensors, and other elements needed to simulate real-world interactions. The properties of each world are defined in a ```.sdf``` file. Further info are documented [here](https://gazebosim.org/docs/latest/sdf_worlds/).

The ```basic_world.sdf``` file is used to setup a simple world with some minor properties, like the gravity pull and a ground plane.

## /launch folder
A launch file is an XML or Python file used to start and configure multiple nodes and other resources in a ROS system. In this case, the ```gazebo_sim.launch.py``` will open the *basic_world.sdf* world, importing in the simulation the robot described in the ```three_joints_arm.xacro``` file, which is defined in the **robot_description** package. In the future it will be developed the option to execute a ```rviz``` node connected to the gazebo simulation. 

## Launch the simulation
To launch the ```gazebo_sim.launch.py``` file, first of all, ensure that in the **CMakeLists.txt** file are present the following line, required to install the */world* and */launch* folders. 
```bash
install(DIRECTORY launch
        DESTINATION share/${PROJECT_NAME}/)

install(DIRECTORY world
        DESTINATION share/${PROJECT_NAME}/)
```
Then, execute in a terminal the command
```bash
ros2 launch robot_gazebo gazebo_sim.launch.py
```

### Additional note
Of course, if you clone this repo, the CMakeLists.txt file will be already correctly formatted, but in case you want to add some new folders with other files, be sure to add 
```bash
install(DIRECTORY "folder_name"
        DESTINATION share/${PROJECT_NAME}/)
```
in the CMakeLists.txt file.