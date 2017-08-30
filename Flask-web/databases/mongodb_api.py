'''
dbpath: ~/data/db
run: mongod --dbpath ~/data/db
'''
import pymongo
from ..config  import dbConfig
import datetime

client = pymongo.MongoClient(dbConfig['url'], dbConfig['port'])
db = client['quant']
collection = db['tradeHistoryData']



