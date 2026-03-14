#!/bin/env/ python

from gpiozero import LED
from time import sleep
import readerLED

# GPIO26 using BCM numbering
pin = LED(26)

# Turn LED Green
readerLED.GLED_on(1)
