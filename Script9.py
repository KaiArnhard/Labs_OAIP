import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = (10,  9, 11,  5,  6, 13, 19, 26)
comp = 4
troyka = 17

GPIO.setup(comp, GPIO.IN) 
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

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
    for value in range(256):
        list1 = decimal_to_bin(value)
        GPIO.output(dac, list1)
        time.sleep(0.001)
        compVal = GPIO.input(comp)
        if compVal == 0:
            print("ADC value = {:^3}, voltage = {:.2f}".format(value, (value / 255) * 3.3))
            break


try:
    while 1:
    
        adc()

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()       
