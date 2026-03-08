#!/bin/env python

from gpiozero import LED
from signal import pause
import sys
import time
import subprocess

# Set LED Blue
BLED = LED(9)

# Set LED Green
GLED = LED(25)

# Set LED Red
RLED = LED(11)

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
        time.sleep(int(X)/factor)
        RLED.off()
        time.sleep(int(X)/factor)

factor=20
# Green LED Blinking for X seconds
def GLED_blink(X):
    for i in range(int(X)):
        GLED.on()
        time.sleep(int(X)/factor)
        GLED.off()
        time.sleep(int(X)/factor)

factor=20
# Blue LED Blinking for X seconds
def BLED_blink(X):
    for i in range(int(X)):
        BLED.on()
        time.sleep(int(X)/factor)
        BLED.off()
        time.sleep(int(X)/factor)

if __name__ == "__main__":
    #globals()[sys.argv[1]](sys.argv[2:])
    func_name = sys.argv[1]
    args = sys.argv[2:]
    globals()[func_name](*args)

#pause()
