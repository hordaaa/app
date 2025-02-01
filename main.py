from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return f"hello world {randint(1, 1000)}"
