# Imports
from machine import ADC, Pin
import time

# GOT ANOTHER POTENTIOMETER THAN IN PDF
# DONT KNOW WHICH PIN IS WHICH...

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))
value = 0
while True: # Loop forever
    value = 65535 - potentiometer.read_u16()
    if (value != 0):
        print(value) # Read the potentiometer value
    time.sleep(0.2) # Wait a second