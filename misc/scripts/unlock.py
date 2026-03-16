#!/bin/env/ python

from gpiozero import LED
from time import sleep
import readerLED

# GPIO26 using BCM numbering
pin = LED(26)

# Unlock remote control signal
pin.on()
sleep(1)
pin.off()

# Turn LED Green
#readerLED.GLED_on(1)
