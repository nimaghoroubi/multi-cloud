def create_file(body):
    pre = """#cloud-config

# run commands
# default: none
# runcmd contains a list of either lists or a string
# each item will be executed in order at rc.local like level with
# output to the console
# - runcmd only runs during the first boot
# - if the item is a list, the items will be properly executed as if
#   passed to execve(3) (with the first arg as the command).
# - if the item is a string, it will be simply written to the file and
#   will be interpreted by 'sh'
#
# Note, that the list has to be proper yaml, so you have to quote
# any characters yaml would eat (':' can be problematic)

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
    -#!/bin/bash
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
    - echo "services ready, cloning repo"
    - sudo git clone https://github.com/nimaghoroubi/multi-cloud /multi
    - echo "clone complete! running services!"
    - (cd /multi && screen -dmS celery celery worker -l info -A addfunction)
            """

    with open("./user-data.txt", 'w+') as ud:
        ud.write(pre + body + content)
