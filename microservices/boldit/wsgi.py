from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def boldit():
    return '<b> {} </b>'.format(request.args.get('msg', ''))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
