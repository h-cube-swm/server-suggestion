from hanspell import spell_checker

with open('surveys.txt','r',encoding='utf-8') as f:
    with open('pretty.txt','w',encoding='utf-8')as o:
        text = f.read()
        for row in text.split('\n'):
            row = row.strip()
            row = spell_checker.check(row).checked
            o.write(row+'\n')