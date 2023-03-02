import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
a = GPIO.input(18)

#for counter in range(100):
GPIO.output(23, a)
#time.sleep(1)

time.sleep(20)
GPIO.cleanup()