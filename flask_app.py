from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/test/<int:parameter_1>', methods=['GET'])
def test(parameter_1):
    return f'This is {parameter_1}.'

@app.route('/index/')
def tweet_index():
    return render_template('index.html')

@app.route('/airfoil/angle/<int:angle>/', methods=['GET'])
def airfoil(angle):
    # if failed:
    #     return jsonify("failed")
    return jsonify('task_id')

@app.route('/airfoil/result/<str:task_id>/', methods=['GET'])
def airfoil_result(task_id):
    # if not ready:
    #     return jsonify('Running + time')
    return jsonify('angle and force lists')
