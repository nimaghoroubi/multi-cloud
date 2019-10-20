from flask import Flask
from flask_celery import make_celery
from addfunction import add
from requests import get
from userdatawriter import create_file

ip = get('https://api.ipify.org').text # get the ip
line = "ip = " + str(ip)

with open("/multi/worker/addfunction.py", 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(line.rstrip('\r\n') + '\n' + content)

create_file(str(ip))


broker = 'amqp://killer:killer@'+str(ip)+'/killer'


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = broker
app.config['CELERY_RESULT_BACKEND'] = 'amqp'

celery = make_celery(app)

@app.route('/')
def test():
    request = add_function.delay(10,20) # the bug lies here, simplify this
    #return_value = request.get()
    #return return_value
    return("hi\n")


@celery.task(name='addfunction.add')
def add_function(a,b):
    data = add(a,b)
    return data

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
