# connect ground (black) to 6, VCC (red) to 1 and control (yellow) to 11

import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # 50 Hz
p.start(2.5)  # init
try:
    while True:
        for i in [5, 7.5, 10, 12.5, 10, 7.5, 5, 2.5]:
            p.ChangeDutyCycle(i)
            time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
