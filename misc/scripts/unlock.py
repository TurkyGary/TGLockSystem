#!/bin/env/ python

from gpiozero import LED
from time import sleep

# GPIO26 using BCM numbering
pin = LED(26)

# Turn ON
pin.on()

# Keep it ON for 1 second
sleep(1)

# Turn OFF
pin.off()

