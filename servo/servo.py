import RPi.GPIO as GPIO  # https://pypi.org/project/RPi.GPIO/
import time


servoPIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.output(servoPIN, True)


class Servo(object):
    def __init__(self, pin, pwm, min_duty, max_duty, center_duty):
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

    def rotate(self, angle):
        if angle not in self.allowed_angles:
            raise Exception('Angle: ' + str(angle) + ' not in allowed angles: ' + str(self.allowed_angles))
        if angle > 0:
            duty = angle / 12 + self.min_duty
        if angle < 0:
            duty = (-1 * angle) / 12 - self.min_duty - 0.5
        if angle == 0:
            duty = 7

        self._gpio.ChangeDutyCycle(duty)
        time.sleep(1)


class TowerProSG90(Servo):
    def __init__(self, pin, min_duty=3.5, max_duty=11, center_duty=7):
        super().__init__(pwm=50, pin=pin, min_duty=min_duty, max_duty=max_duty, center_duty=center_duty)
        self.allowed_angles = range(-90, 91, 1)


servo = TowerProSG90(pin=servoPIN)
servo.start()
try:
    while True:
        servo.rotate(0)
        time.sleep(1)
        servo.rotate(90)
        time.sleep(1)
        servo.rotate(-90)
        break

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
