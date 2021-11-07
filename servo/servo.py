import RPi.GPIO as GPIO  # https://pypi.org/project/RPi.GPIO/


class Servo(object):
    def __init__(self, pin: int, pwm, min_duty, max_duty, center_duty):
        self._gpio = GPIO.PWM(pin, pwm)
        self.pin = pin
        self.pwm = pwm
        self.min_duty = min_duty  # -90 degrees
        self.max_duty = max_duty  # +90 degrees
        self.center_duty = center_duty  # 0 degrees
        self.allowed_angles = []

    def start(self):
        self._gpio.start(0)

    def stop(self):
        self._gpio.stop()

    def rotate(self, angle: float):
        if angle not in self.allowed_angles:
            raise Exception('Angle: ' + str(angle) + ' not in allowed angles: ' + str(self.allowed_angles))
        if angle > 0:
            duty = angle / 12 + self.min_duty
        if angle < 0:
            duty = (-1 * angle) / 12 - self.min_duty - 0.5
        if angle == 0:
            duty = 7

        self._gpio.ChangeDutyCycle(duty)
