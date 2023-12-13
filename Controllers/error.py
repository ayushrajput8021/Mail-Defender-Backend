from flask import Flask, json

app = Flask(__name__)


def page_not_found(e):
    res_data = {'Status': 'Success', 'Message': f'Error: {e}'}
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=404,
        mimetype='application/json'
    )
    return res_send
