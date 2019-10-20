from celery import Celery

broker_adress = 'amqp://killer:killer@'+ip+'/killer'

app = Celery('tasks', backend='amqp',
broker = broker_adress)

@app.task
def add(x, y):
    return x + y
