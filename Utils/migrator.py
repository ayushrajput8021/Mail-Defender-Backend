# from dotenv import load_dotenv
# load_dotenv()
# import pymongo
# import os
# from supabase import Client, create_client
# # import uuid
#
#
# url = str(os.getenv("SUPABASE_URL"))
# key = str(os.getenv("SUPABASE_KEY"))
# supabase: Client = create_client(url, key)
#
# db_url: str = os.getenv("MONGO_URL")
# db_user: str = os.getenv("MONGO_USERNAME")
# db_pass: str = os.getenv("MONGO_PASSWORD")
# db_name: str = os.getenv("MONGO_DB_NAME")
#
# # altering the db url for parameters
# db_url = db_url.replace('<USERNAME>', db_user)
# db_url = db_url.replace('<PASSWORD>', db_pass)
# db_url = db_url.replace('<DATABASE>', db_name)
#
# # db connection
# myClient = pymongo.MongoClient(db_url)
# mydb = myClient["Emailer-Data"]
# mycol = mydb["main-data"]
#
# # i=0
# # for x in mycol.find():
#     # i=i+1
#     # data = supabase.table('main_data').insert({"Category": x['Category'], "Message": x['Message']}).execute()
#     # data= supabase.table('acc_data').insert({"id": i, "Accuracy-Train": x['Accuracy-Train'], "Accuracy-Test": x['Accuracy-Test'],"Train-size": x['Train-size'],"Test-size": x['Test-size']}).execute()
#
# # response = supabase.table('acc_data').select("*").execute()
# # print(response)
