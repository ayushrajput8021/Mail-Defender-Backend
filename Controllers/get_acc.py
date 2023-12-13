from flask import Flask, json

from Database.main_data import get_acc

app = Flask(__name__)


def get_accu():
    res_data = get_acc()
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=200,
        mimetype='application/json'
    )
    return res_send
