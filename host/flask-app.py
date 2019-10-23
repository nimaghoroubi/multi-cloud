from flask import Flask, jsonify, request
from flask_celery import make_celery
import json
from addfunction import add
from requests import get
from userdatawriter import create_file
import tasks

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
    request = add_function.delay(10, 20)
    request.ready()
    return_value = request.get()
    return return_value


@app.route('/problems/<problem_id>',)
def problem_route(problem_id):

    # solver_id = from request
    parameters = {
        "S": [90, 100, 110],
        "K": 100,
        "T": 1.0,
        "r": 0.03,
        "sig": 0.15,
    }

    if problem_id == "1":
        print('parameters: ', parameters)
        S = parameters["S"]
        K = parameters["K"]
        T = parameters["T"]
        r = parameters["r"]
        sig = parameters["sig"]
        print("S: ", S)
        res = problem1.delay(S, K, T, r, sig)
        result = res.get()
        print("RES: ", result)

    response = {}
    response["problemID"] = problem_id
    response["result"] = json.loads(result)
    return jsonify(response)


@celery.task(name='addfunction.add')  # this name is important, investigate
def add_function(a, b):
    data = add(a, b)
    return data


@celery.task(name="tasks.problem1")
def problem1(S, K, T, r, sig):
    return tasks.problem1(S, K, T, r, sig)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
