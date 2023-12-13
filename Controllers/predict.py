from flask import Flask, request, json

from spam_predictor import Predict

app = Flask(__name__)


def receive_data():
    data = request.get_json()
    response_data = Predict(data['message'])
    response = int(str(response_data[0]))
    res_data = {'Status': 'Success', 'Response': 'Spam' if response == 0 else 'Ham'}
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=200,
        mimetype='application/json'
    )
    return res_send
