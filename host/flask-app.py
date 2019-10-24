from flask import Flask, jsonify, request
from flask_celery import make_celery
import json
from addfunction import add
from requests import get
from userdatawriter import create_file
import tasks
import time

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
    #request.ready()
    #return_value = request.get()
    return "You are at the right place\n"


@app.route('/problems/<problem_id>',)
def problem_route(problem_id):
    result = {}
    # solver_id = from request
    if problem_id == "1":
        while True:
            res = problem1.delay()
            try:
                result = json.loads(res.get())
                print(result)
                if result['failure'] is False:
                    break
            except:
                result['result'] = "solver did not function as expected"
            time.sleep(1)

    print("RES: ", result)
    response = {}
    response["problemID"] = problem_id
    response["result"] = result['result']
    return jsonify(response)


@celery.task(name='addfunction.add')  # this name is important, investigate
def add_function(a, b):
    data = add(a, b)
    return data


@celery.task(name="tasks.problem1")
def problem1(S = [90, 100, 110], K = 100, T = 1, r = 0.03, sig = 0.15):
    return tasks.problem1(S, K, T, r, sig)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
