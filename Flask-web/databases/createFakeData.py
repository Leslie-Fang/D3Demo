import datetime
import random
import time
import pymongo
from config import dbConfig

year = ["16"]
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
day = range(1,31)
if __name__ == "__main__":
    client = pymongo.MongoClient(dbConfig['url'], dbConfig['port'])
    db = client['quant']
    collection = db['tradeHistoryData']
    count = 1
    basePrice = 0.8
    startTime = datetime.datetime.now()
    for itemY in year:
        for itemM in month:
            for itemD in day:
                price = basePrice + random.random()*0.1 + (datetime.datetime.now() - startTime).seconds*0.01
                tradeEvent = {'date': str(str(itemD) + "-" + itemM + "-" + itemY), "MarketCurrency": "LTC", "BaseCurrency": "BTC", "price": price}
                # print(collection.find_one())
                id = collection.insert_one(tradeEvent).inserted_id
                print id
                time.sleep(1)
