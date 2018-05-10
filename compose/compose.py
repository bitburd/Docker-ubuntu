import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=80)


@app.route('/')
def hello():
    return 'Hello World!\n'

if __name__ == "__main__":
    app.run(host="192.168.1.15", debug=True)
