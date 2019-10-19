from celery import Celery

app = Celery('tasks', backend='amqp',
broker='amqp://killer:killer@34.230.81.244/killer')

def add(x, y):
    return x + y
