def AddTemp(cat,msg):
  import pymongo
  import pandas as pd
  myclient = pymongo.MongoClient("mongodb+srv://admin:ayush6420@cluster0.zrmn96t.mongodb.net/Emailer?retryWrites=true&w=majority")
  mydb = myclient["Emailer-Data"]
  mycol = mydb["temp-data"]
  # mycol.update_many({'Category':'spam'},{'$set':{'Category':'0'}})
  # mycol.update_many({'Category':'ham'},{'$set':{'Category':'1'}})
  # data = [[cat,msg]] 
  # df = pd.DataFrame(data, columns=['Category','Message']) 
  # records_ = df.to_dict(orient = 'records') 
  # mycol.insert_many(records_ )
AddTemp(0,'hello')