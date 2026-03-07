#!/bin/env python
from gpiozero import DigitalInputDevice
from gpiozero import LED
from signal import pause
import time
import subprocess

# Powered by GPIO24
SensorPin = LED(24)
SensorPin.on()
#time.sleep(5)

# Connected to GPIO10 for input digital signal
sensor = DigitalInputDevice(10, pull_up=False, bounce_time=0.01)

def card_detected():
    print("card detected!")
#    SensorPin.off()
#    time.sleep(5)
#    SensorPin.on()
    subprocess.run(["readIDcard"])
    time.sleep(3)

def path_clear():
    print("Path is clear.")

# Assign functions to events
#sensor.when_activated = path_clear
#sensor.when_deactivated = card_detected
sensor.when_activated = card_detected

print("IR Sensor Active... Press Ctrl+C to exit")
pause()
