import json
from glob import glob
from flask import Flask, request, jsonify, render_template
from tasks import airfoil_task, get_task

app = Flask(__name__)

RESULT_FOLDER = "/home/ubuntu/ACC-7/result"


@app.route('/test/<int:parameter_1>', methods=['GET'])
def test(parameter_1):
    return f'This is {parameter_1}.'

@app.route('/index/')
def tweet_index():
    return render_template('index.html')

@app.route('/airfoil/submit/', methods=['POST'])
def airfoil():
    parameters = request.get_json()
    print(parameters)
    angle = parameters.get("angle")
    n_nodes = parameters.get("n_nodes", 100)  # 100
    n_levels = parameters.get("n_levels", 0)  # 0
    speed = parameters.get("speed", 10)  # 10
    time = parameters.get("time", 0.5)  # 0.05
    persisted_result = f"{RESULT_FOLDER}/a{angle}n{n_nodes}l{n_levels}s{speed}t{time}.json"
    if glob(persisted_result):  # TODO: task submission when the same setting is running but not ready yet.
        with open(persisted_result) as f:
            data = json.load(f)
        return jsonify({"status": "RESULT", "data": data})
    task = airfoil_task.delay(angle, n_nodes, n_levels, speed, time)
    return jsonify({"status": task.status, "task_id": task.id})

@app.route('/airfoil/result/<string:task_id>/', methods=['GET'])
def airfoil_result(task_id):
    task = get_task(task_id)
    if task.ready():
        data = task.get()
        persisted_result = f"{RESULT_FOLDER}/a{data['angle']}n{data['n_nodes']}l{data['n_levels']}s{data['speed']}t{data['time']}.json"
        with open(persisted_result, 'w') as outfile:
            json.dump(data, outfile)
        return jsonify({"status": "RESULT", "data": data})
    else:
        return jsonify({"status": task.status})
