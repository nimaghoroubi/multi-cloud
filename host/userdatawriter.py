def create_file(body):  # body is ip of host server, this creates the cloud config file
    pre = """#cloud-config
write_files:
  - path: /home/ubuntu/tasks.py
    content: |
        from celery import Celery
        from oct2py import Oct2Py
        import json

        octave = Oct2Py()
        octave.addpath('/multi/BENCHOP/RBF-FD')
        # octave.addpath('/multi/BENCHOP/RBF-FD')
        # octave.addpath('/multi/BENCHOP/RBF-FD')

        broker_adress = 'amqp://killer:killer@"""

    content = """/killer'
        app = Celery('tasks', backend='amqp',
        broker = broker_adress)
        @app.task
        def problem1(S, K, T, r, sig):
            print('problem1')
            res = json.dumps(octave.BSeuCallUI_RBFFD(S, K, T, r, sig).tolist())
            print('res:', res)
            return res




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
    - sudo apt install octave -y &&
    - sudo apt install git -y &&
    - sudo python -m pip install oct2py &&
    - sudo git clone https://github.com/nimaghoroubi/multi-cloud.git &&
    - cd /multi
    - sudo git checkout parameters-playground &&
    - screen -dmS celery celery worker -l info -A tasks
            """

    with open("/home/ubuntu/user-data.txt", 'w+') as ud:
        ud.write(pre + body + content)
