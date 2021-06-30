from flask import Flask

print('Start flask app!')

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!...I'm alive!"

if __name__ == '__main__':
    app.run(debug=True)