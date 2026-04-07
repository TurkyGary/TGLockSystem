#!/bin/env python

from gpiozero import LED
from signal import pause
import sys
import os
import time
import subprocess

# Set LED Blue
BLED = LED(9)

# Set LED Green
GLED = LED(25)

# Set LED Red
RLED = LED(11)

# Red LED ON
def RLED_ON():
    RLED.on()
    os._exit(0)

# Green LED ON
def GLED_ON():
    GLED.on()
    os._exit(0)

# Blue LED ON
def BLED_ON():
    BLED.on()
    os._exit(0)

# Turn OFF all LEDs
def LEDs_off():
    RLED.off()
    GLED.off()
    BLED.off()
    os._exit(0)

# Cycle RGB
def cycle_rgb(X):
    RLED.on()
    time.sleep(0.5)
    RLED.off()
    GLED.on()
    time.sleep(0.5)
    GLED.off()
    BLED.on()
    time.sleep(0.5)
    BLED.off()

# Turn ON Red LED for X seconds
def RLED_on(X):
    RLED.on()
    time.sleep(int(X))
    RLED.off()

# Turn ON Green LED for X seconds
def GLED_on(X):
    GLED.on()
    time.sleep(int(X))
    GLED.off()

# Turn ON Blue LED for X seconds
def BLED_on(X):
    BLED.on()
    time.sleep(int(X))
    BLED.off()

factor=20
# Red LED Blinking for X seconds
def RLED_blink(X):
    for i in range(int(X)):
        RLED.on()
        time.sleep(0.06)
        RLED.off()
        time.sleep(0.125)

# Green LED Blinking for X seconds
def GLED_blink(X):
    for i in range(int(X)):
        GLED.on()
        time.sleep(0.06)
        GLED.off()
        time.sleep(0.125)

# Blue LED Blinking for X seconds
def BLED_blink(X):
    for i in range(int(X)):
        BLED.on()
        time.sleep(0.06)
        BLED.off()
        time.sleep(0.125)

# Help
def help():
    print(f"Usage:\npython {sys.argv[0]} [OPTION]\n\nOptions:\n    - RLED_on : Turn Red LED on\n    - GLED_on : Turn Green LED on\n    - BLED_on : Turn Blue LED on\n    - LEDs_off : Turn off all LEDs\n    - cycle_rgb X : Turn on/off RGB LEDs for X seconds\n    - RLED_on X : Turn on Red LED for X seconds\n    - GLED_on X : Turn on Green LED for X seconds\n    - BLED_on X : Turn on Blue LED for X seconds\n    - RLED_blink X : Red LED blining for X seconds\n    - GLED_blink X : Green LED blinking for X seconds\n    - BLED_blink X : Blue LED blinking for X seconds\n")


# Call methods from command prompt
if __name__ == "__main__":
    #globals()[sys.argv[1]](sys.argv[2:])
    func_name = sys.argv[1]
    args = sys.argv[2:]
    globals()[func_name](*args)

#pause()
