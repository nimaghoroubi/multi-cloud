#!/bin/bash
echo "starting ******************************************************************"
echo "installing updates"
sudo apt-get update &&
sudo apt-get -y upgrade &&
echo "installing python"
sudo apt-get -y install python &&
echo "installing and upgrading pip"
sudo apt -y install python-pip &&
sudo python -m pip install --upgrade pip &&
echo "installing celery"
sudo python -m pip install celery &&
echo "services ready, cloning repo"
sudo git clone https://github.com/nimaghoroubi/multi-cloud /worker-service &&
echo "clone complete! running services!"
