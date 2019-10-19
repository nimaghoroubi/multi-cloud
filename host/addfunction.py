from celery import Celery

app = Celery('tasks', backend='amqp',
broker='amqp://guest@34.230.81.244')

@app.task
def add(x, y):
    return x + y
