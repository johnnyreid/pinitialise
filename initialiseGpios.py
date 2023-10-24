#!/usr/bin/python3

import pigpio
from loguru import logger

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

# GPIO BCM details:
# lawn   GPIO#s: 0, 1, 2, 3, 4, 5
# garden GPIO#s: 6, 7, 21, 22

pins = [17, 27, 22, 23, 18, 24,
        25, 4, 5, 6]

logger.add("/var/logs/pinitialise/{time:YYYYMMDD}.log")

pi = pigpio.pi()       # access the local Pi's GPIO

logger.info("GPIO Initialisation started at {time:HH:mm}.---------------------------")

for pin in pins:
    pi.set_mode(pin, pigpio.OUTPUT)  # GPIO 17 as output
    logger.info("Pin {pinNumber}'s current value is {pinValue}", pinNumber=str(pin), pinValue=str(pi.read(pin)))

    pi.write(pin, 0)
    logger.info("Pin {pinNumber} should be off: {pinValue}", pinNumber=str(pin), pinValue=str(pi.read(pin)))

    pi.write(pin, 1)
    logger.info("Pin {pinNumber} should be on: {pinValue}", pinNumber=str(pin), pinValue=str(pi.read(pin)))

    logger.info("Initialisation completed for pin {}! \n", str(pin))

logger.info("GPIO Initialisation completed at {time:HH:mm}.---------------------------")
