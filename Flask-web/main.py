from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/test')
def test():
    return render_template('test.html')
