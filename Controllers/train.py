from flask import Flask, request, json

from Database.main_data import check_auth
from model_trainer import train

app = Flask(__name__)


def train_data():
    data = request.get_json()
    username = data['id']
    password = data['pass']
    if check_auth(username, password):
        train()
        res_data = {'Status': 'Success', 'Message': 'Trained'}
        status = 200
    else:
        res_data = {'Status': 'Not Authenticated', 'Message': 'Training model is failed'}
        status = 401
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=status,
        mimetype='application/json'
    )
    return res_send
