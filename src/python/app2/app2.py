from flask import Flask
from what_time import handler
from wsgi_runner import run

app = Flask(__name__)


@app.route("/")
def time():
    return handler()

if __name__ == '__main__':
    options = {'bind': '0.0.0.0:5001'}
    run(app, options)
