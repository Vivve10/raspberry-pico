# Imports
from machine import Pin, PWM
import time

# Btns
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)
# Lights
green_small = Pin(25, Pin.OUT)
green_big = Pin(19, Pin.OUT)
yellow = Pin(20, Pin.OUT)
# Buzzer
buzzer = PWM(Pin(13))

# Tunes
C = 523
D = 587
E = 659
G = 784
# Volume (Duty cycle)
volume = 1000

def play(tune):
    buzzer.duty_u16(volume)
    buzzer.freq(tune)
    time.sleep(0.1)
    buzzer.duty_u16(0)


while True:
    time.sleep(0.01) # Short Delay
        
    if button1.value() == 1: # If button 1 is pressed
        
        print("Button 1 pressed")
        green_small.toggle()
        play(G)
        
    if button2.value() == 1: # If button 2 is pressed
        
        print("Button 2 pressed")
        yellow.toggle()
        play(D)
        
    if button3.value() == 1: # If button 3 is pressed
        
        print("Button 3 pressed")
        green_big.toggle()
        play(C)