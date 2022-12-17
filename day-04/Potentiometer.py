# Imports
from machine import ADC, Pin
import time

# GOT ANOTHER POTENTIOMETER THAN IN PDF
# DONT KNOW WHICH PIN IS WHICH...

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

while True: # Loop forever

    print(potentiometer.read_u16()) # Read the potentiometer value

    time.sleep(1) # Wait a second