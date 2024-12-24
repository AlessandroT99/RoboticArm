cmake_minimum_required(VERSION 3.30)
project(RoboticArm)

set(CMAKE_CXX_STANDARD 14)

include_directories(robot_arm_ws/src/robot_arm/include)

add_executable(RoboticArm
    robot_arm_ws/src/robot_arm/include/PIDController.h
    robot_arm_ws/src/robot_arm/src/PIDController.cpp)
