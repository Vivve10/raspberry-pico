from machine import Pin
import time

green_small = Pin(25, Pin.OUT)

green_big = Pin(19, Pin.OUT)
yellow = Pin(20, Pin.OUT)

repetitions = 100
num = 0

print("start blink")
while num < repetitions:
    num = num + 1
    print(num)
    if (num % 3 == 0):
        green_big.value(1)
        green_small.value(0)
        yellow.value(0)
    if (num % 3 == 1):
        green_big.value(0)
        green_small.value(1)
        yellow.value(0)
    if (num % 3 == 2):
        green_big.value(0)
        green_small.value(0)
        yellow.value(1)
    time.sleep(0.1)
print("stop blink")

# Turn all lamps off
green_big.value(0)
green_small.value(0)
yellow.value(0)




run_port_test = False
number = 0
if (run_port_test):
    print("test all ports")
    while number < 29:
        print(number)
        pin = Pin(number, Pin.OUT)
        pin.value(1)
        time.sleep(0.4)
        number = number + 1


