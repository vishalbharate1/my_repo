import pymongo
import pandas as pd
import os, sys
import json
from dataclasses import dataclass

@dataclass
class EnvironmentVaribale:
    mongo_db_url=os.getenv('MONGO_DB_URL')

env_var=EnvironmentVaribale()
mongo_client= pymongo.MongoClient(env_var.mongo_db_url)
TARGRT_COLOUMN='v1'
print(env_var.mongo_db_url)