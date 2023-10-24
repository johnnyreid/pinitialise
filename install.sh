#!/bin/bash

[[ $(id -u) = "0" ]] || { echo "Please run the script as root user. sudo $0"; exit; }

echo "Installing pinitialise and its dependencies...."

# Install dependencies
apt-get -y install python3-pigpio python3-loguru

#Start and enable the auto-start on boot
systemctl enable pigpiod
systemctl start pigpiod

# (Re)Install the pinitialise service
if [ -f /etc/systemd/system/pinitialise.service ]; then
    sudo systemctl stop pinitialise.service
    sudo systemctl disable pinitialise.service
fi

sudo \cp -f ./pinitialise.service /etc/systemd/system/pinitialise.service


#Start and enable the auto-start on boot
sudo systemctl enable pinitialise.service
sudo systemctl start pinitialise.service

# Make the logs directory
if [ ! -d /var/logs/pinitialise ]; then
  sudo mkdir /var/logs/pinitialise
fi

echo "Installation complete."
