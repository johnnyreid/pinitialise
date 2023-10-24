#!/bin/bash

[[ $(id -u) = "0" ]] || { echo "Please run the script as root user. sudo $0"; exit; }

echo "Uninstalling pinitialise and its dependencies...."

# Stop, disable and remove the pinitialise service
if [ -f /etc/systemd/system/pinitialise.service ]; then
    sudo systemctl stop pinitialise.service
    sudo systemctl disable pinitialise.service
    rm /etc/systemd/system/pinitialise.service
fi

#Stop and disable the pigpiod auto start
systemctl stop pigpiod
systemctl disable pigpiod

#Remove about everything regarding the package packagename, but not the dependencies installed with it on installation.
apt-get purge -y python3-pigpio

#Remove orphaned packages, i.e. installed packages that used to be installed as an dependency, but aren't any longer. Use this after removing a package which had installed dependencies you're no longer interested in.
apt-get -y autoremove

echo "Uninstallation complete."