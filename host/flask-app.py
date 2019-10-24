from flask import Flask, jsonify, request
from flask_celery import make_celery
import json
from addfunction import add
from requests import get
from userdatawriter import create_file
import tasks
import time
from scheduler import schedule

ip = get('https://api.ipify.org').text  # get the ip
line = "ip = " + str(ip)


create_file(str(ip))  # cloud config file


broker = 'amqp://killer:killer@'+str(ip)+'/killer'


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = broker
app.config['CELERY_RESULT_BACKEND'] = 'amqp'

celery = make_celery(app)


@app.route('/')
def test():
    #request = add_function.delay(10, 20)
    # request.ready()
    #return_value = request.get()
    return "You are at the right place\n"


@app.route('/problems/<problem_id>/<solver_name>',)
def problem_route(problem_id, solver_name):
    parameters = request.args
    counter = 0
    while True:
        counter = counter + 1
        res = schedule_creator.delay(solver_name, problem_id, parameters)
        try:
            result = json.loads(res.get())
            print(result)
            if result['failure'] is False:
                break
        except:
            result['result'] = "solver did not function as expected"
            #print("we are in except")
        #print("we are before sleep")
        time.sleep(1)
        if counter > 10:
            result['result'] = "exceeded time limit"
            break

    print("RES: ", result)
    response = {}
    response["problemID"] = problem_id
    response["result"] = result['result']
    return jsonify(response)


@celery.task(name='addfunction.add')  # this name is important, investigate
def add_function(a, b):
    data = add(a, b)
    return data


@celery.task(name="tasks.schedule_creator")
def schedule_creator(solver_name, problem_id, parameters):
    return shedule(solver_name, problem_id, parameters)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
