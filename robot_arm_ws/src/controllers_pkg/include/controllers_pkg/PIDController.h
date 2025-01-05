//
// Created by riccardo on 12/24/24.
//

#ifndef PIDCONTROLLER_H
#define PIDCONTROLLER_H
#include <string>

// ==============================================================================
// Class
// ==============================================================================

class PIDController {

public:

    // ==============================================================================
    // Constructor and Destructor
    // ==============================================================================
    PIDController(const std::string &joint_name, double kp, double ki, double kd);

    // ==============================================================================
    // Additional Functions
    // ==============================================================================
    double compute(double target, double current, double dt);

private:

    // ==============================================================================
    // Variables
    // ==============================================================================
    std::string joint_name_ = "JointWithoutName";
    double kp_, ki_, kd_;       // PID coefficient
    double previousError_;      // for the derivative part
    double integral_;           // sum of the errors for the integral part
    double output_ = 0;
};

#endif // PIDCONTROLLER_H