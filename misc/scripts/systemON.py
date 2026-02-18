from gpiozero import LED
from signal import pause

# GPIO4 is referred to by its Broadcom (BCM) number
pin = LED(4)

# Turn it ON
pin.on()

# print("GPIO4 is now ON. Press Ctrl+C to exit.")
pause()

