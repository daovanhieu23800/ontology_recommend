from flask import Flask, request, jsonify
from spraql_topic import SpraqlTopic
from spraql_LM import SpraqlLM, Style
import requests

app = Flask(__name__)


@app.route("/topic", methods=['GET', 'POST'])
def get_topic():
    if request.method == 'GET':
        return "jsonify(result)"

    elif request.method == 'POST':
        data = request.get_json()

        if data.get("startID") and data.get("endID") and data.get("rdf_path"):
            startID = data["startID"]
            endID = data["endID"]
            rdf_path = data["rdf_path"]
        spraql = SpraqlTopic(startID, endID, rdf_path)
        paths = spraql.spraqlTopic()

        result = {"paths": paths}
        return jsonify(result)


@app.route("/material", methods=['GET', 'POST'])
def get_material():
    if request.method == 'GET':
        return "jsonify(result)"
    elif request.method == 'POST':
        result = {}

        request_data = request.get_json()

        startID = request_data["startID"]
        endID = request_data["endID"]

        body_data = {
            "startID": startID,
            "endID": endID,
            "rdf_path": "./rdf/draft-topic-onto.rdf"
        }

        response = requests.post('http://127.0.0.1:5000/topic', json=body_data)
        learning_path = []
        data = response.json()
        for v in data.values():
            learning_path += v

        # print(learning_path)
        learning_style = Style(
            qualification=request_data["learner_style"]["qualification"],
            backgroundKnowledge=request_data["learner_style"]["backgroundKnowledge"],
            active_reflective=request_data["learner_style"]["active_reflective"],
            visual_verbal=request_data["learner_style"]["visual_verbal"],
            global_sequential=request_data["learner_style"]["global_sequential"],
            sensitive_intuitive=request_data["learner_style"]["sensitive_intuitive"]
        )
        lm_rdf_path = "./rdf/draft-system-onto.rdf"

        spraql = SpraqlLM(lm_rdf_path, learning_path)
        lm_recommend = spraql.spraql_lm(learning_style)

        for i in range(len(lm_recommend)):
            key = f"path_{i+1}"
            result[key] = lm_recommend[i][0]

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
