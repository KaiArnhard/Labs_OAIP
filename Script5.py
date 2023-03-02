import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

list1 = (21, 20, 16, 12, 7, 8, 25, 24)  
aux   = (22, 23, 27, 18, 15, 14, 3, 2)

try:
    GPIO.setup(list1, GPIO.OUT)
    GPIO.setup(aux, GPIO.IN)

    GPIO.output(list1, 1)

    while 1:
        for i in range(len(aux)):
            GPIO.output(list1[i], GPIO.input(aux[i]))
finally:
    GPIO.output(list1, 0)
    GPIO.cleanup()       
