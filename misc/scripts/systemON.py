from gpiozero import LED
from signal import pause
from datetime import datetime

# GPIO4 is referred to by its Broadcom (BCM) number
pin = LED(4)

# Turn it ON
pin.on()

# Writing to logs
#now = datetime.now()
#timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")
#with open("/home/ecel2b40/Documents/TGLockSystem/logs/startup.log", "w") as file:
#	file.write(f"[{timestamp}] TGLockSystem is ready.\n")

# print("GPIO4 is now ON. Press Ctrl+C to exit.")
pause()

