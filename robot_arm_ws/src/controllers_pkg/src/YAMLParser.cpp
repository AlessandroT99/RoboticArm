//
// Created by riccardo on 1/5/25.
//

#include "YAMLParser.h"

#include <rclcpp/logging.hpp>

YAMLParser::YAMLParser(const std::string& file_path) : file_path_(file_path)
{

}

std::vector<PIDController> YAMLParser::loadControllersConfiguration() const
{
    std::vector<PIDController> *controllers = nullptr;

    try {
        YAML::Node config = YAML::LoadFile(file_path_);

        if (!config["joints"]) {
            RCLCPP_ERROR(rclcpp::get_logger("PIDConfigLoader"), "Chiave 'joints' non trovata nel file YAML!");
            return *controllers;
        }

        for (const auto &joint : config["joints"]) {
            PIDController joint_config(
                joint["name"].as<std::string>(),
                joint["kp"].as<double>(),
                joint["ki"].as<double>(),
                joint["kd"].as<double>()
            );
            controllers->push_back(joint_config);
        }

    } catch (const YAML::Exception &e) {
        RCLCPP_ERROR(rclcpp::get_logger("PIDConfigLoader"), "Error while parsing the YAML file: %s", e.what());
    }
    return *controllers;
}
