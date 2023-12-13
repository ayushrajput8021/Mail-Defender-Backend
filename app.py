from dotenv import load_dotenv
from flask import Flask

load_dotenv()
from flask_cors import CORS
from model_trainer import *
from Controllers.home_page import *
from Controllers.login import admin_login
from Controllers.get_acc import get_acc
from Controllers.add_temp import add_temp
from Controllers.predict import receive_data
from Controllers.train import train_data
from Controllers.error import page_not_found

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def route_home():
    return home_page()


@app.route('/login', methods=['POST'])
def route_admin_login():
    return admin_login()


@app.route('/get-acc', methods=['GET'])
def route_get_accu():
    return get_acc()


@app.route('/predict', methods=['POST'])
def route_receive_data():
    return receive_data()


@app.route('/train', methods=['POST'])
def route_train_data():
    return train_data()


@app.route('/add-temp', methods=['POST'])
def route_add_temp():
    return add_temp()


@app.errorhandler(404)
def route_page_not_found(e):
    return page_not_found(e)


port = os.getenv("PORT")

if __name__ == '__main__':
    app.run()
