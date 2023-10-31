import pymongo
import pandas as pd
import datetime
import hashlib

myclient = pymongo.MongoClient(
    "mongodb+srv://admin:ayush6420@cluster0.zrmn96t.mongodb.net/Emailer?retryWrites=true&w=majority")
mydb = myclient["Emailer-Data"]
mycol = mydb["main-data"]

# updating data
# mycol.update_many({'Category':'spam'},{'$set':{'Category':'0'}})
# mycol.update_many({'Category':'ham'},{'$set':{'Category':'1'}})

# for record in mycol.find():
#     print(record)
# cursor = mycol.find({}, {"Category": 1})
# data_list = [document["Category"] for document in cursor]
# data_series = pd.Series(data_list)
# print(data_series)
# df = pd.read_csv("master_data.csv")
# records_ = df.to_dict(orient = 'records')
# result = mycol.insert_many(records_ )


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

def check_auth(username,password):
    password=password.encode()
    sha256 = hashlib.sha256()
    sha256.update(password)
    mycol = mydb["auth-data"]
    token = sha256.hexdigest()
    user = mycol.find_one({'username': username})
    if user and 'password' in user and user['password'] == token:
        return True
    else:
        return False

def save_temp(cat,msg):
    mycol = mydb["temp-data"]
    return bool(mycol.insert_one({'Category':cat,'Message':msg}))