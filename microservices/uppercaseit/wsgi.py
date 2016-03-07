from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return request.args.get('msg', '').upper()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
