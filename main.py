from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "Введите http://127.0.0.1:5000/Recruto/давай дружить "

@app.route('/<string:name>/<string:phrase>')
def task(name, phrase):
    return "Hello {}! ".format(name)+"{}!".format(phrase)
