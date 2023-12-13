from flask import Flask, request, json

from Database.main_data import save_temp

app = Flask(__name__)


def add_temp():
    data = request.get_json()
    if save_temp(data['Category'], data['Message']):
        res_data = {'Status': 'Success', 'Message': 'Data saved in DB'}
        status = 201
    else:
        res_data = {'Status': 'Failed', 'Message': 'Error in saving data in DB'}
        status = 400
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=status,
        mimetype='application/json'
    )
    return res_send
