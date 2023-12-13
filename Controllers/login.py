from flask import Flask, request, json

from Database.main_data import check_auth

app = Flask(__name__)


def admin_login():
    data = request.get_json()
    if check_auth(data['username'], data['password']):
        res_data = {'Status': 'Authenticated'}
        status = 200
    else:
        res_data = {'Status': 'Not Authenticated'}
        status = 401
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=status,
        mimetype='application/json'
    )
    return res_send
