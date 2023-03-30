import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = (21, 20, 16, 12, 7, 8, 25, 24)
dac = (10,  9, 11,  5,  6, 13, 19, 26)
comp = 4
troyka = 17

GPIO.setup(comp, GPIO.IN) 
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT)

def get_number():
    while 1:
        number = input(("enter number: "))
        if number.isdecimal() == 0:
            print("Not decimal number")
            continue
        if number == 'q':
            break
        if int(number) < 0:
            print("Less then zero")
            continue
        elif int(number) > 255:
            print("More then 255")
            continue
        try: 
            x = int(number)
            return x
        except ValueError:
            print("you entered not a number")


def decimal_to_bin(x):
    string = format(x, 'b')
    tmp_list1 = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(string)):
        tmp_list1[i] = int(string[len(string) - (i + 1)])
    return tmp_list1 


def adc():
    sum = 0
    value = 0
    for k in range(7, 0, -1):
        value = 2 ** k
        sum += value
        list1 = decimal_to_bin(sum)
        GPIO.output(dac, list1)
        time.sleep(0.001)
        compVal = GPIO.input(comp)
        if compVal == 0:
            sum -= value
    print("ADC value = {:^3}, voltage = {:.2f}".format(sum, (sum / 255) * 3.3))
    return value

try:
    while 1:
        ledsvalue = adc()
        list2 = decimal_to_bin(ledsvalue)
        GPIO.output(leds, list2)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, 0)
    GPIO.cleanup()       
