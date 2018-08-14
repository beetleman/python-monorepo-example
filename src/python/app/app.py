from flask import Flask
from helloworld import handler
from wsgi_runner import run

app = Flask(__name__)


@app.route("/")
def hello():
    return handler()


if __name__ == '__main__':
    options = {'bind': '0.0.0.0:5000'}
    run(app, options)
