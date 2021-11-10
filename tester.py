import json
import numpy as np
from preprocess import initialize, normalize
from sklearn.feature_extraction.text import TfidfVectorizer

initialize()

with open('parsed.json', 'r', encoding='utf-8') as f:
    tokenized_list = json.loads(f.read())

keys = []
docs = []

for data in tokenized_list:
    key = data['tokens']
    obj = data['object']
    keys.append(key)
    docs.append(obj)

tfidfv = TfidfVectorizer().fit(keys)
keys = tfidfv.transform(keys).toarray()


def get_order(text, num=10):
    normalized = normalize(text)
    vector = tfidfv.transform([normalized]).toarray()[0]
    result = []
    for i in range(len(docs)):
        dist = np.dot(vector, keys[i])
        result.append([dist, docs[i]])
    result.sort(key=lambda x: -x[0])
    return result[:num]
