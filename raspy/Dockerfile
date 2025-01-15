FROM ros:jazzy-ros-core

RUN apt-get update 
RUN apt-get install ros-$ROS_DISTRO-demo-nodes-py -y
RUN apt-get install ros-$ROS_DISTRO-demo-nodes-cpp
RUN bash -c "source /opt/ros/$ROS_DISTRO/local_setup.bash"
RUN export ROS_DOMAIN_ID=0

CMD [ "ros2", "run", "demo_nodes_cpp", "talker" ]

