import RPi.GPIO as GPIO
import time
import math

dac    = [26, 19, 13, 6,  5, 11, 9,  10]
leds   = [21, 20, 16, 12, 7, 8,  25, 24]
comp   = 4
troyka = 17

MAX_VOLTAGE = 3.3

RANK = 8
MAX_VALUE = 2 ** RANK

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac,    GPIO.OUT)
GPIO.setup(leds,   GPIO.OUT)
GPIO.setup(comp,   GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def dec2bin (value, rank):
    assert(isinstance(value, int))
    assert(isinstance(rank,  int))

    return [int(element) for element in bin(value)[2:].zfill(rank)]

def adc ():
    left  = -1
    right = MAX_VALUE + 1

    while True:
        mid = int((left + right) / 2)

        GPIO.output(dac, dec2bin(mid, RANK))

        time.sleep(0.05)

        if GPIO.input(comp) == 0:
            right = mid
        else:
            left  = mid

        if right - left <= 1:
            return mid

def get_volume (number):
    percent = number % RANK

    array = [0] * RANK
    for i in range(percent):
        array[i] = 1

    GPIO.output(leds, array)


try:
    while 1:
        value = adc()
        get_volume(value)

finally:
    GPIO.output(dac,    0)
    GPIO.output(leds,   0)
    GPIO.output(troyka, 0)

    GPIO.cleanup()

