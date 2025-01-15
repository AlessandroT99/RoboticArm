import RPi.GPIO as GPIO
import time

# GPIO setup
SERVO_PIN = 18  # GPIO pin connected to the servo signal wire
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize PWM on the servo pin
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz for servo control
pwm.start(0)

def set_angle(angle):
    """
    Set the servo angle.
    :param angle: Desired angle between 0 and 180 degrees.
    """
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Allow time for the servo to reach the position
    pwm.ChangeDutyCycle(0)  # Stop sending signal to prevent jitter

try:
    angle = 0
    direction = 1  # 1 for increasing angle, -1 for decreasing angle
    print("Press Enter to move the servo. Ctrl+C to exit.")

    while True:
        input("Press Enter to move the servo...")  # Wait for Enter key
        set_angle(angle)
        print(f"Servo set to {angle}°")

        # Update angle
        angle += direction * 10
        if angle >= 180 or angle <= 0:
            direction *= -1  # Reverse direction when limits are reached

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    pwm.stop()
    GPIO.cleanup()
