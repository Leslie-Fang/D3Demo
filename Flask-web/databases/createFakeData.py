import datetime
import random
import time

from mongodb_api import collection

if __name__ == "__main__":
    count = 1
    basePrice = 0.8
    startTime = datetime.datetime.now()
    while count < 100:
        price = basePrice + random.random()*0.1 + (datetime.datetime.now() - startTime).seconds*0.01
        tradeEvent = {'date': datetime.datetime.now(), "MarketCurrency": "LTC", "BaseCurrency": "BTC", "price": price}
        # print(collection.find_one())
        id = collection.insert_one(tradeEvent).inserted_id
        print id
        time.sleep(1)
        count = count +1