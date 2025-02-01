from flask import Flask
from random import randint
from redis import Redis


app = Flask(__name__)

redis_cli = Redis()

@app.route("/")
def index():
    rand_number = randint(1, 10)
    flag = redis_cli.get(str(rand_number))
    if not flag: redis_cli.setex(str(rand_number), 60, str(rand_number))
    return f"{rand_number} cached? {flag}"
