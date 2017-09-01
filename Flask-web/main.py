from flask import Flask
from flask import render_template
from flask import url_for
from databases.mongodb_api import getHistoryData
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/showData')
def showData():
    return render_template('showData.html')

@app.route('/getData')
def getData():
    data = getHistoryData()
    #write data 2 csv
    # with open('./static/data2.tsv',"w+") as f:
    #     f.write("date\tprice\ttradePair\n")
    #     print(data)
    #     for i in range(1,350):
    #         print i
    #         cData = data[i]
    #         print cData
    #         print(cData["price"])
    #         f.write(cData["date"]+"\t"+str(cData["price"])+"\t"+cData["tradePair"]+"\t\n")
    ret = json.dumps(data)
    return ret
