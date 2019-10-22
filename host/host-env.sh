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
sudo git clone https://github.com/nimaghoroubi/multi-cloud /multi &&
# ######################### setting login for rabbitmq
# add new user
sudo rabbitmqctl add_user killer killer &&
# add new virtual host
sudo rabbitmqctl add_vhost killer &&
# set permissions for user on vhost
sudo rabbitmqctl set_permissions -p killer killer ".*" ".*" ".*" &&
# restart rabbit
sudo service rabbitmq-server restart &&
# ######################### starting the service which creates cloud config file
screen -dmS host sudo python /multi/host/flask-app.py &&
# ######################### installing aws and creating instances with config file
sudo snap install  aws-cli --classic &&
sleep 10 &&
echo "aws installed after wait" &&
/snap/bin/aws configure set default.region us-east-1 && echo "zone configured" ;
/snap/bin/aws ec2 run-instances --image-id ami-04b9e92b5572fa0d1 --count 1 --instance-type t2.micro --key-name multi  --security-groups multi --user-data file:///user-data.txt &&
echo "worker launched" &&
sudo echo "Reached end" >> ~/final.txt
