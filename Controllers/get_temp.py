from flask import Flask, json

from Database.main_data import get_temp_data

app = Flask(__name__)


def get_temp():
    res_data = get_temp_data()
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=200,
        mimetype='application/json'
    )
    return res_send
