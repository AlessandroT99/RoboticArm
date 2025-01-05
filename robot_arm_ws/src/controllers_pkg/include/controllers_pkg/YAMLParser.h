//
// Created by riccardo on 1/5/25.
//

#ifndef YAMLPARSER_H
#define YAMLPARSER_H

#include <yaml-cpp/yaml.h>
#include <string>
#include <PIDController.h>

class YAMLParser{

public:
    YAMLParser(const std::string &file_path);
    ~YAMLParser();

    std::vector<PIDController> loadControllersConfiguration() const;

private:

    std::string file_path_;
};

#endif //YAMLPARSER_H
