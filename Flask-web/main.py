from flask import Flask
from flask import render_template
from flask import url_for
from databases.mongodb_api import getHistoryData
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')

@app.route('/test3')
def test3():
    return render_template('test3.html')

@app.route('/getData')
def getData():
    ret = getHistoryData()
    return ret
