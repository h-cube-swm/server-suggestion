from hanspell import spell_checker  
from konlpy.tag import Kkma
tokenizer=Kkma()

with open('surveys.txt','r',encoding='utf-8') as f:
    with open('parsed.txt','w',encoding='utf-8')as o:
        text = f.read()
        for row in text.split('\n'):
            row = row.strip()
            if len(row)<2:
                continue

            row = spell_checker.check(row).checked
            tokens = tokenizer.morphs(row)
            data = row+"<SPLIT>"+' '.join(tokens)
            print(data)
            o.write(data+'\n')