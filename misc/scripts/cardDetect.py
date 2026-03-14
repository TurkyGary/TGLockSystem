#!/bin/env python
from gpiozero import DigitalInputDevice
from gpiozero import LED
from signal import pause
import time
import subprocess

# Powered by GPIO24
SensorPin = LED(24)
SensorPin.on()

# Connected to GPIO10 for input digital signal
sensor = DigitalInputDevice(10, pull_up=False, bounce_time=0.01)

def card_detected():
    print("card detected!")
    subprocess.run(["readIDcard"])
    time.sleep(3)

def card_clear():
    print("Place card to read.")

# Assign functions to events
sensor.when_deactivated = card_clear
sensor.when_activated = card_detected

print("IR Sensor Active... Press Ctrl+C to exit")
pause()
