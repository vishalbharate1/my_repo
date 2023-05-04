import pymongo
import pandas as pd
import numpy as np
import json

uri = "mongodb+srv://vishalbharate1:vishal123@cluster0.zih76bz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = pymongo.MongoClient(uri)

#File_Name='datasets_483_982_spam.csv'
Data_File_Path=(r'C:\Users\visha\data science\myrepo\my_repo\datasets_483_982_spam.csv')
Database_Name='SMS_My_Repo'
Collection_Name='SMS_Data'


if __name__ == '__main__':
    df=pd.read_csv(Data_File_Path)
    print(f'Rows and columns in database are: {df.shape}')
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[Database_Name][Collection_Name].insert_many(json_record)

