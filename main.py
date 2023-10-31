from flask import Flask, jsonify, request
from predictor import *
from main_data import check_auth,save_temp

app = Flask(__name__)
app.config.from_pyfile('/settings.py')

@app.route('/',methods=['GET'])
def home_page():
    return '<h1>Home Page</h1>'

@app.route('/login',methods=['POST'])
def admin_login():
    data = request.get_json()
    if check_auth(data['username'],data['password']):
        return 'Authenticated'
    else:
        return 'Not Authenticated'

@app.route('/predict', methods=['POST'])
def receive_data():
    data = request.get_json()
    response_data = Predict(data['message'])
    response = int(str(response_data[0]))
    res_obj = {'Status': 'Ok', 'Response': response}
    return res_obj


@app.route('/train', methods=['POST'])
def train_data():
    data = request.get_json()
    id = data['id']
    password = data['pass']
    if (id == 'admin' and password == 'admin123'):
        return 'Authorised'
    else:
        return 'Unauthorised Route'

@app.route('/add-temp',methods=['POST'])
def add_temp():
    data = request.get_json()
    if save_temp(data['Category'],data['Message']):
        return 'Saved to DB'
    else:
        return 'Error in saving to DB'
    