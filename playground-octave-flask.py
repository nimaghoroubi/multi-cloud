from flask import Flask, jsonify, request
from something import *
import json

app = Flask(__name__)


@app.route('/problems/<problem_id>',)
def test(problem_id):

    # solver_id = from request
    parameters = {
        "S": [90, 100, 110],
        "K": 100,
        "T": 1.0,
        "r": 0.03,
        "sig": 0.15,
    }

    response = {}
    response["problemID"] = problem_id
    response["result"] = json.loads(somethingFunction(problem_id, parameters))
    return jsonify(response)


if __name__ == '__main__':
    print("Server is up and running")
    app.run('0.0.0.0', debug=True)
