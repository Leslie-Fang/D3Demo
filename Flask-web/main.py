from flask import Flask
from flask import render_template
from flask import url_for
from databases.mongodb_api import getHistoryData
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')

@app.route('/test3')
def test3():
    return render_template('test3.html')

@app.route('/getData')
def getData():
    ret = getHistoryData()
    #write data 2 csv
    with open('./static/data2.tsv',"w+") as f:
        f.write("date\tprice\n")
        data = json.loads(ret)
        print(data)
        for i in range(1,350):
            print i
            print(data[str(i)])
            cData = data[str(i)]
            print(cData["price"])
            f.write(cData["date"]+"\t"+str(cData["price"])+"\t\n")

    return ret
