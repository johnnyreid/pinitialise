#!/bin/bash

[[ $(id -u) = "0" ]] || { echo "Please run the script as root user. sudo $0"; exit; }

echo "Installing pinitialise and its dependencies...."

#update apt database
apt-get update

# Install dependencies including pigpio: https://abyz.me.uk/rpi/pigpio/python.html
apt-get -y install python3-pigpio python3-pip

#install loguru: https://github.com/Delgan/loguru
pip install loguru

#Start and enable the auto-start on boot
systemctl enable pigpiod
systemctl start pigpiod

# (Re)Install the pinitialise service
if [ -f /etc/systemd/system/pinitialise.service ]; then
    systemctl stop pinitialise.service
    systemctl disable pinitialise.service
fi

cp -f ./pinitialise.service /etc/systemd/system/pinitialise.service

#Start and enable the auto-start on boot
systemctl enable pinitialise.service
systemctl start pinitialise.service

echo "Installation complete."
