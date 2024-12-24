//
// Created by riccardo on 12/24/24.
//

#ifndef PIDCONTROLLER_H
#define PIDCONTROLLER_H

class PIDController {
public:
    // Costruttore
    PIDController(double kp, double ki, double kd)
        : kp_(kp), ki_(ki), kd_(kd), prev_error_(0.0), integral_(0.0) {}

    // Metodo per calcolare l'output PID
    double compute(double target, double current, double dt);

private:
    double kp_, ki_, kd_;         // Coefficienti PID
    double prev_error_;           // Errore precedente
    double integral_;             // Somma degli errori per la componente integrale
};

#endif // PIDCONTROLLER_H
