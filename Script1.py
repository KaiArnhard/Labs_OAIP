import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
for i in range(10):
    GPIO.output(23, 1)
    time.sleep(1)
    GPIO.output(23, 0)
    time.sleep(1)
time.sleep(10)
GPIO.cleanup()