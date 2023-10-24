#!/usr/bin/python3

import pigpio
from loguru import logger
from datetime import datetime

# Reference for pigpio library: https://abyz.me.uk/rpi/pigpio/

# This is a Raspberry Pi 1 Model B+
# GPIO | PIN | Broadcom number (used by pigpio)
# 0    | 11  | 17
# 2    | 13  | 27
# 3    | 15  | 22
# 4    | 16  | 23
# 1    | 12  | 18
# 5    | 18  | 24
# 6    | 22  | 25
# 7    | 7   | 4
# 8    | 29  | 5
# 9    | 31  | 6

logger.add("/var/logs/pinitialise/{time:YYYYMMDD}-initialiseGpios.log")
logger.info("--- GPIO Initialisation started at {current_time} ---", current_time=datetime.now().strftime("%H:%M:%S"))

# GPIO BCM details:
# lawn   GPIO#s: 0, 1, 2, 3, 4, 5
# garden GPIO#s: 6, 7, 21, 22
pins = [17, 27, 22, 23, 18, 24,
        25, 4, 5, 6]
pi = pigpio.pi()       # access the local Pi's GPIO

for pin in pins:
    logger.info("Initialising pin {}...", str(pin))
    pi.set_mode(pin, pigpio.OUTPUT)
    logger.info("    Pin {pinNumber}'s current value is {pinValue}", pinNumber=str(pin), pinValue=str(pi.read(pin)))
    # pi.write(pin, 1)
    # logger.info("    Pin {pinNumber} should now be on: {pinValue}", pinNumber=str(pin), pinValue=str(pi.read(pin)))
    pi.write(pin, 0)
    logger.info("    Pin {pinNumber} should now be off: {pinValue}", pinNumber=str(pin), pinValue=str(pi.read(pin)))
    logger.info("Initialisation completed for pin {}! \n", str(pin))

logger.info("--- GPIO Initialisation completed at {current_time} ---", current_time=datetime.now().strftime("%H:%M:%S"))

# Release pigpio resources
pi.stop()
