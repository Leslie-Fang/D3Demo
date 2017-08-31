import datetime
import random
import time
import pymongo
from config import dbConfig

if __name__ == "__main__":
    client = pymongo.MongoClient(dbConfig['url'], dbConfig['port'])
    db = client['quant']
    collection = db['tradeHistoryData']
    count = 1
    basePrice = 0.8
    startTime = datetime.datetime.now()
    while count < 100:
        price = basePrice + random.random()*0.1 + (datetime.datetime.now() - startTime).seconds*0.01
        tradeEvent = {'date': str(datetime.datetime.now()), "MarketCurrency": "LTC", "BaseCurrency": "BTC", "price": price}
        # print(collection.find_one())
        id = collection.insert_one(tradeEvent).inserted_id
        print id
        time.sleep(1)
        count = count +1