import RPi.GPIO as GPIO
import time

from servo.tower_pro_sg90 import TowerProSG90


servoPIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.output(servoPIN, True)


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
