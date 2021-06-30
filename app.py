from flask import Flask, request
from tester import get_order
import json

app = Flask(__name__,static_url_path='', static_folder='static',)

@app.route('/')
def home():
    return "IM ALIVE"

@app.route('/test', methods=['POST'])
def order():    
    text = request.json['text']
    print(text)
    order = get_order(text)
    stringified = json.dumps(order)
    return stringified

if __name__ == '__main__':
    app.run(debug=True)