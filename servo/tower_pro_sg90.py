from servo.servo import Servo


class TowerProSG90(Servo):
    def __init__(self, pin, min_duty=3.5, max_duty=11, center_duty=7):
        super().__init__(pwm=50, pin=pin, min_duty=min_duty, max_duty=max_duty, center_duty=center_duty)
        self.allowed_angles = range(-90, 91, 1)
