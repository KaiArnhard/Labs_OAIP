import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = (10,  9, 11,  5,  6, 13, 19, 26)        
list1 = [0, 0, 0, 0, 0, 0, 0, 0]

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

    for i in range(len(string)):
        list1[i] = int(string[len(string) - (i + 1)])
        

try:
    GPIO.setup(dac, GPIO.OUT)
    
    while 1:
        for i in range(256):
            decimal_to_bin(i)
            GPIO.output(dac, list1)
            time.sleep(0.3)
        for k in range(256):
            decimal_to_bin(255 - k)
            GPIO.output(dac, list1)
            time.sleep(0.3)
            

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()       

