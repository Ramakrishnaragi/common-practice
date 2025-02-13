
import boto4

from flask import *

app = Flask(__name__)
port=5000
@app.route('/')
def home():
    return "<h1>Welcome to Jenkins Tutorials<h1/>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0'
