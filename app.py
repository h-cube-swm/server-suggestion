from flask import Flask, request, send_file
from tester import get_order
import json

app = Flask(__name__,static_url_path='', static_folder='static',)

@app.route('/')
def home():
    return send_file('static/index.html')

@app.route('/test', methods=['POST'])
def order():    
    text = request.json['text'].strip()
    if(len(text)>2):
        order = get_order(text)[:10]
    else:
        order = []
    stringified = json.dumps(order)
    return stringified

if __name__ == '__main__':
    app.run(debug=True)