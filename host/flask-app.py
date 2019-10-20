from flask import Flask
from flask_celery import make_celery
from addfunction import add

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://killer:killer@34.230.81.244/killer'

celery = make_celery(app)

@app.route('/')
def addfunction(10,20):
    request = add_function.delay(10,20)
    return_value = request.get()
    return return_value


@celery.task(name='add_function.add')
def add_function(a,b):
    data = add(a,b)
    return data

if __name__ == '__main__':
    app.run('0.0.0.0')
