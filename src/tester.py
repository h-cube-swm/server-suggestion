import json
import numpy as np
from preprocess import initialize, normalize
from sklearn.feature_extraction.text import TfidfVectorizer

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
print('Tester initialization finished.')


def get_order(text, num=10):
    normalized = normalize(text)
    vector = tfidfv.transform([normalized]).toarray()[0]
    result = []
    for i in range(len(docs)):
        similarity = np.dot(vector, keys[i])
        if similarity < 0.4:
            continue
        result.append([similarity, docs[i]])
    result.sort(key=lambda x: -x[0])
    return result[:num]
