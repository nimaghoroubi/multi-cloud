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
echo "installing rabbitmq"
sudo apt -y install rabbitmq-server &&
echo "installing celery"
sudo python -m pip install celery &&
echo "installing openstack"
sudo python -m pip install python-openstackclient &&
echo "installing flask"
sudo apt -y install python-flask &&
echo "services ready, cloning repo"
sudo git clone https://github.com/nimaghoroubi/multi-cloud /multi
# add new user
sudo rabbitmqctl add_user killer killer &&
# add new virtual host
sudo rabbitmqctl add_vhost killer &&
# set permissions for user on vhost
sudo rabbitmqctl set_permissions -p killer killer ".*" ".*" ".*" &&
# restart rabbit
sudo service rabbitmq-server restart &&
screen -dmS host sudo python /multi/host/flask-app.py
sudo apt snap aws-cli --classic &&
aws configure set default.region eu-north-1
#sample boot:
#   aws ec2 run-instances --image-id ami-1dab2163 --count 1 --instance-type t3.micro --key-name EC2  --security-groups launch-wizard-2
