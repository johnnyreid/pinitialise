#!/usr/bin/python3

import pigpio
from loguru import logger
from datetime import datetime

# Reference for pigpio library: https://abyz.me.uk/rpi/pigpio/

# This is a Raspberry Pi 1 Model B+
# Relay | GPIO# | PIN | Broadcom number (used by pigpio)
# 1     | 0     | 11  | 17
# 2     | 1     | 13  | 27
# 3     | 2     | 15  | 22
# 4     | 3     | 16  | 23
# 5     | 4     | 12  | 18
# 6     | 5     | 18  | 24
# 7     | 6     | 22  | 25
# 8     | 7     | 7   | 4
# 9     | 21    | 29  | 5

#Not in use:
# 10    | 22    | 31  | 6
# 11    | 23    | 33  | 13
# 12    | 24    | 35  | 19
# 13    | 25    | 37  | 26
# 14    | 26    | 32  | 12
# 15    | 27    | 36  | 16
# 16    | 28    | 38  | 20

# GPIO BCM details:
# lawn   GPIO#s: 0, 1, 2, 3, 4, 5
# garden GPIO#s: 6, 7, 21, 22

# ##### NOTE: ##########
# 0 = relay on
# 1 = relay off
########################

logger.add("/var/logs/pinitialise/{time:YYYYMMDD}-initialiseGpios.log")
logger.info("--- GPIO Initialisation started at {current_time} ---",
            current_time=datetime.now().strftime("%H:%M:%S"))

pi = pigpio.pi()       # access the local Pi's GPIO

pins = [17, 27, 22, 23, 18, 24,
        25, 4, 5, 
        6, 13, 19, 26, 12, 16, 20]

for pin in pins:
    logger.info("Initialising pin {}...", str(pin))
    pi.set_mode(pin, pigpio.OUTPUT)
    logger.info("    Pin {pinNumber}'s current value is {pinValue}",
                pinNumber=str(pin), pinValue=str(pi.read(pin)))
    pi.write(pin, 1)
    logger.info("    Pin {pinNumber} should now be 1 (which means relay is off): {pinValue}",
                pinNumber=str(pin), pinValue=str(pi.read(pin)))
    # pi.write(pin, 0)
    # logger.info("    Pin {pinNumber} should now be 0 (which means relay is on): {pinValue}",
    #             pinNumber=str(pin), pinValue=str(pi.read(pin)))
    logger.info("Initialisation completed for pin {}! \n", str(pin))

logger.info("--- GPIO Initialisation completed at {current_time} ---",
            current_time=datetime.now().strftime("%H:%M:%S"))

# Release pigpio resources
pi.stop()
