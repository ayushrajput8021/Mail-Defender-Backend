import pandas as pd
import os
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

# importing db credentials
url = str(os.getenv("SUPABASE_URL"))
key = str(os.getenv("SUPABASE_KEY"))
supabase: Client = create_client(url, key)


def X_data():
    response = supabase.table('main_data').select("Message").execute()
    data_series = pd.Series([d['Message'] for d in response.data])
    return data_series


def Y_data():
    response = supabase.table('main_data').select("Category").execute()
    data_series = pd.Series([d['Category'] for d in response.data])
    return data_series


def save_acc(acc_train, acc_test, X_train, X_test):
    supabase.table('acc_data').insert(
        {"Accuracy_Train": acc_train, "Accuracy_Test": acc_test, "Train_size": X_train, "Test_size": X_test}).execute()


def get_acc():
    response = supabase.table('acc_data').select("*").execute()
    for entry in response.data:
        if 'created_at' in entry:
            created_at = entry["created_at"]
            date, time = created_at.split('T')
            time = time.split('.')
            entry.pop('created_at', None)
            entry.pop('id', None)
            entry['Date'] = date
            entry['Time'] = time[0]
    return response.data


def check_auth(username, password):
    response = supabase.table('auth-data').select('*').execute()
    user = response.data[0]['username']
    pwd = response.data[0]['password']
    if user == username and password == pwd:
        return True
    else:
        return False


def save_temp(cat, msg):
    if supabase.table('temp-data').insert({"Category": cat, "Message": msg}).execute():
        return True
    else:
        return False


def get_temp_data():
    response = supabase.table('temp-data').select('*').execute()
    for entry in response.data:
        entry.pop('id', None)
    return response.data


def temp_to_main():
    response = supabase.table('temp-data').select('*').execute()
    for x in response.data:
        supabase.table('test_main_data').insert({"Category": x['Category'], "Message": x['Message']}).execute()

