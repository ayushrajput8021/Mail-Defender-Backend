from dotenv import load_dotenv
from flask import Flask, request, Response, json

load_dotenv()
from spam_predictor import *
from flask_cors import CORS
from model_trainer import *

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home_page():
    return '<h1>Home Page</h1>'


@app.route('/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if check_auth(data['username'], data['password']):
        res_data = {'Status': 'Authenticated'}
    else:
        res_data = {'Status': 'Not Authenticated'}
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=200,
        mimetype='application/json'
    )
    return res_send


@app.route('/get-acc', methods=['GET'])
def get_accu():
    res_data = get_acc()
    res_send = app.response_class(
        response=json.dumps(res_data),
        status=200,
        mimetype='application/json'
    )
    return res_send



@app.route('/predict', methods=['POST'])
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


@app.route('/train', methods=['POST'])
def train_data():
    data = request.get_json()
    username = data['id']
    password = data['pass']
    if check_auth(username, password):
        train()
        return Response("Trained", status=400, mimetype='application/json')
    else:
        return Response({'Status': 'Not Authenticated'}, status=401, mimetype='application/json')


@app.route('/add-temp', methods=['POST'])
def add_temp():
    data = request.get_json()
    if save_temp(data['Category'], data['Message']):
        return 'Saved to DB'
    else:
        return 'Error in saving to DB'


@app.errorhandler(404)
def page_not_found(e):
    return Response("404", status=404, mimetype='application/text')


port = os.getenv("PORT")

if __name__ == '__main__':
    app.run(port=3000, debug=True)
