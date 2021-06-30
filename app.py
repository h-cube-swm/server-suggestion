from flask import Flask
from hanspell import spell_checker
from konlpy.tag import Kkma  

kkma=Kkma()  

def tokenizer(text):
    text= spell_checker.check(text).checked
    text = kkma.morphs(text)
    return text

app = Flask(__name__)

@app.route('/')
def home():
    return "IM ALIVE"

if __name__ == '__main__':
    app.run(debug=True)