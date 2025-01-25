cmake_minimum_required(VERSION 3.8)
project(controllers_pkg)

# Abilita C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Trova i pacchetti necessari
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# Includi la directory degli header
include_directories(include/controllers_pkg)

# Aggiungi il file sorgente
add_library(controllers_pkg
        src/PIDController.cpp
        src/JointControllers.cpp
        src/YAMLParser.cpp)

target_link_libraries(controllers_pkg rclcpp::rclcpp)

# Specifica la directory di installazione degli header
install(DIRECTORY include/ DESTINATION include)

# Specifica la directory di installazione della libreria
install(TARGETS controllers_pkg
        DESTINATION lib)

# Informa ament del target da installare
ament_export_dependencies(rclcpp)
ament_export_include_directories(include)
ament_export_libraries(controllers_pkg)

# Finalizza il pacchetto
ament_package()
