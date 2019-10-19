from celery import Celery

app = Celery('tasks', backend='amqp',
broker='amqp://add@34.230.81.244/add')

@app.task
def add(x, y):
    return x + y
