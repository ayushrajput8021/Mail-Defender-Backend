import pymongo
import pandas as pd
import datetime
import hashlib
import os

#importing db crediantials
db_url: str = os.getenv("MONGO_URL")
db_user: str = os.getenv("MONGO_USERNAME")
db_pass: str = os.getenv("MONGO_PASSWORD")
db_name: str = os.getenv("MONGO_DB_NAME")

# altering the db url for parameters
db_url = db_url.replace('<USERNAME>', db_user)
db_url = db_url.replace('<PASSWORD>', db_pass)
db_url = db_url.replace('<DATABASE>', db_name)

#db connection
myclient = pymongo.MongoClient(db_url)
mydb = myclient["Emailer-Data"]
mycol = mydb["acc-data"]

def X_data():
    cursor = mycol.find({}, {"Message": 1})
    data_list = [document["Message"] for document in cursor]
    data_series = pd.Series(data_list)
    return data_series


def Y_data():
    cursor = mycol.find({}, {"Category": 1})
    data_list = [document["Category"] for document in cursor]
    data_series = pd.Series(data_list)
    return data_series


def save_acc(acc_train, acc_test, X_train, X_test):
    date = datetime.datetime.now()
    mycol = mydb["acc-data"]
    mycol.insert_one(
        {'date': date, 'Accuracy-Train': acc_train, 'Accuracy-Test': acc_test, 'Train-size': X_train, 'Test-size': X_test})


def check_auth(username, password):
    password = password.encode()
    sha256 = hashlib.sha256()
    sha256.update(password)
    mycol = mydb["auth-data"]
    token = sha256.hexdigest()
    user = mycol.find_one({'username': username})
    if user and 'password' in user and user['password'] == token:
        return True
    else:
        return False


def save_temp(cat, msg):
    mycol = mydb["temp-data"]
    return bool(mycol.insert_one({'Category': cat, 'Message': msg}))
