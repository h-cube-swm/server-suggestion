import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

docs = []
with open('pretty.txt','r',encoding='utf-8') as f:
    for row in f:
        row = row.strip()
        docs.append(row)

tfidfv = TfidfVectorizer().fit(docs)
docs_v = tfidfv.transform(docs)

def get_closest(text):
    vector = tfidfv.transform([text]).toarray()[0]

    min_value = float('inf')
    min_index = 0

    for i in range(len(docs)):
        sub = vector-docs_v[i]
        l = np.linalg.norm(sub)

        if l < min_value:
            min_value=l
            min_index=i

    return docs[min_index]

def get_order(text):
    vector = tfidfv.transform([text]).toarray()[0]
    result = []
    for i in range(len(docs)):
        sub = vector-docs_v[i]
        l = np.linalg.norm(sub)
        result.append([l,docs[i]])
    result.sort(key=lambda x:x[0])
    return result