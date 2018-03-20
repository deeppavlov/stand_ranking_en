import json
from flask import Flask, request, jsonify, redirect
from flasgger import Swagger
from flask_cors import CORS

from ranking_agent import RankingAgent


app = Flask(__name__)
Swagger(app)
CORS(app)
agent = None


@app.route('/')
def index():
    return redirect('/apidocs/')


@app.route('/score', methods=['GET'])
def score():
    """
    Run Ranking model on specified tasks number
    ---
    parameters:
      - name: tasks_number
        in: query
        required: true
        type: string
    """
    tasks_number = request.args.get('tasks_number')

    if not tasks_number.isdigit() or int(tasks_number) <= 0:
        return jsonify({
            'error': 'tasks_number must be an integer, greater then zero'
        }), 400

    result = agent.answer(int(tasks_number))

    return jsonify(result), 200


@app.route('/answer', methods=['POST'])
def answer_ranking():
    """
    Ranking (English)
    ---
    parameters:
     - name: data
       in: body
       required: true
       type: json
    """
    return answer()


def answer():
    if not request.is_json:
        return jsonify({
            "error": "request must contains json data"
        }), 400

    text1 = request.get_json().get('text1') or ""

    if text1 == "":
        return jsonify({
            "error": "request must contains non empty 'text1' parameter"
        }), 400

    task = [text1]
    result = agent.answer(task)
    if isinstance(result, dict) and result.get("ERROR"):
        return jsonify(result), 400

    return jsonify(result), 200


if __name__ == "__main__":
    with open('ranking_agent_config.json') as config_json:
        config = json.load(config_json)
    host = config['api_host']
    port = config['api_port']
    debug = bool(config['api_debug'])
    agent = RankingAgent(config)
    agent.init_agent()
    app.run(host=host, port=port, debug=debug)
