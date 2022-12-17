from machine import Pin
import time

# program to display numbers from 1 to 5

# initialize the variable
i = 10
n = 1

onboardLED = Pin(25, Pin.OUT)

# while loop from i = 1 to 5
while i >= n:
    print(i)
    i = i - 1
    onboardLED.value(0)
    time.sleep(0.5)
    onboardLED.value(1)
    time.sleep(0.5)
