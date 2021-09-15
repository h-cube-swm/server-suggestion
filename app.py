from flask import Flask, request, send_file
from flask_cors import CORS
from tester import get_order
import json

app = Flask(__name__,static_url_path='', static_folder='static',)
cors = CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/')
def home():
    return send_file('static/index.html')

@app.route('/test', methods=['POST'])
def order():
    text = request.json['text'].strip()
    if(len(text)>2):
        _order = get_order(text)
    else:
        _order = []
    stringified = json.dumps(_order)

    return stringified

if __name__ == '__main__':
    app.run(debug=True)