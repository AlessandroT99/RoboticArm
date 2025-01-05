//
// Created by riccardo on 1/5/25.
//

#include "JointControllers.h"

JointControllers::JointControllers() : Node("arm_controllers")
{

    const YAMLParser controllerConfig("paht/to/file");

    controllers = controllerConfig.loadControllersConfiguration();


    }



}
