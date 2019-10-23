def create_file(body): # body is ip of host server, this creates the cloud config file
    pre = """#cloud-config
write_files:
  - path: /multi/addfunction.py
    content: |
        from celery import Celery
        broker_adress = 'amqp://killer:killer@"""

    content = """/killer'
        app = Celery('tasks', backend='amqp',
        broker = broker_adress)
        @app.task
        def add(x, y):
            return x + y



runcmd:
    - echo "starting ******************************************************************"
    - echo "installing updates"
    - sudo apt-get update &&
    - sudo apt-get -y upgrade &&
    - echo "installing python"
    - sudo apt-get -y install python &&
    - echo "installing and upgrading pip"
    - sudo apt -y install python-pip &&
    - sudo python -m pip install --upgrade pip &&
    - echo "installing celery"
    - sudo python -m pip install celery &&
    - (cd /multi && screen -dmS celery celery worker -l info -A addfunction)
            """

    with open("/home/ubuntu/user-data.txt", 'w+') as ud:
        ud.write(pre + body + content)
