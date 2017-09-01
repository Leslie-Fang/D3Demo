'''
dbpath: ~/data/db
run: mongod --dbpath ~/data/db
'''
import pymongo
from config import dbConfig

def getHistoryData():
    client = pymongo.MongoClient(dbConfig['url'], dbConfig['port'])
    db = client['quant']
    collection = db['tradeHistoryData']
    lines = collection.find()
    data = []
    for line in lines:
        #format the date to this format:  Thu Aug 31 2017 20:04:03
        #dataRecord = line['date'].strip().split('.')[0].strip()
        data.append({'date':line['date'],'tradePair':line['MarketCurrency']+'/'+line['BaseCurrency'],'price':line['price']})
        #data[dataCount] = {'date': line['date'],'price': line['price']}
    client.close()
    print data
    return data


if __name__ == "__main__":
    getHistoryData()



