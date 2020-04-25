
Here you will find all the files necessary for the BENCHOPaaS! 

Start with host-env and launch a host machine with it as cloud-config file! (Right now the workers are configured to run on EC2). Remember that in order for your host to be able to function, you need a full EC2 IAM Role connected to it so that it can spawn new workers. 

Give the host enough time, even about or more than 10 minutes, to boot up as the host takes a really long time to boot. The workers will take about 2-3 minutes as they are much lighter than the host.

Check the flask-app.py as a reference for routes until we add a comprehensive guide here! 

Have fun!
