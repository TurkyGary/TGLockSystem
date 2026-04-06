#!/bin/env python

from gpiozero import Buzzer
from time import sleep
import sys

# Set GPIO(1) as the Buzzer signal
buzzer = Buzzer(1)

# SUCCESS: Buzzing for 1/8 of a second
def cardRead_success():
    buzzer.on()
    sleep(0.125)
    buzzer.off()

# FAIL: Buzzing twice for 1/2 of a second
def cardRead_fail():
    buzzer.on()
    sleep(0.125)
    buzzer.off()
    sleep(0.06)
    buzzer.on()
    sleep(0.125)
    buzzer.off()

# REGISTER: Buzzing three times for 1/3 of a second
def cardRegister():
    buzzer.on()
    sleep(0.06)
    buzzer.off()
    sleep(0.125)
    buzzer.on()
    sleep(0.06)
    buzzer.off()
    sleep(0.125)
    buzzer.on()
    sleep(0.06)
    buzzer.off()

# Call methods from command prompt
if __name__ == "__main__":
    #globals()[sys.argv[1]](sys.argv[2:])
    func_name = sys.argv[1]
    args = sys.argv[2:]
    globals()[func_name](*args)
