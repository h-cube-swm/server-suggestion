import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Kkma
from hanspell import spell_checker  
tokenizer=Kkma()

docs = []
vecs = []

with open('parsed.txt','r',encoding='utf-8') as f:
    for row in f:
        row = row.strip()
        if len(row)<2:
            continue
        doc, vec = row.split('<SPLIT>')
        docs.append(doc)
        vecs.append(vec)

tfidfv = TfidfVectorizer().fit(vecs)
vecs = tfidfv.transform(vecs)

def get_order(text,num=10):
    text = spell_checker.check(text).checked
    text = ' '.join(tokenizer.morphs(text))
    vector = tfidfv.transform([text]).toarray()[0]
    result = []
    for i in range(len(docs)):
        sub = vector-vecs[i]
        l = np.linalg.norm(sub)
        result.append([l,docs[i]])
    result.sort(key=lambda x:x[0])
    return result[:num]