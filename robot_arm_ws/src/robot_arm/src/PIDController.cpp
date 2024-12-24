//
// Created by riccardo on 12/24/24.
//

#include "PIDController.h"

PIDController::PIDController(double kp, double ki, double kd)
    : kp_(kp), ki_(ki), kd_(kd), previousError_(0.0), integral_(0.0) {}

double PIDController::compute(double target, double current, double dt) {
    double currentError = target - current;
    integral_ += currentError * dt;
    double derivative = (dt > 0.0) ? (currentError - previousError_) / dt : 0.0;
    previousError_ = currentError;

    output_ = (kp_ * currentError) + (ki_ * integral_) + (kd_ * derivative);

    return output_;
}
