import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

list1 = (21, 20, 16, 12, 7, 8, 25, 24)

GPIO.setup(list1, GPIO.OUT)

for k in range(3):
    for i in range(len(list1)):
        GPIO.output(list1[i], 1)
        time.sleep(0.2)
        GPIO.output(list1[i], 0)
        time.sleep(0.2)
    time.sleep(5)

GPIO.output(list1, 0)
GPIO.cleanup()