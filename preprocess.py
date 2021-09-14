from hanspell import spell_checker
from konlpy.tag import Kkma
import json

SPLITTER = '<SPLIT>'


def run():
    tokenizer = Kkma()
    with open('surveys.json', 'r', encoding='utf-8') as f:
        with open('parsed.txt', 'w', encoding='utf-8')as o:
            json_text = f.read()
            survey_list = json.loads(json_text)
            for survey in survey_list:
                title = survey["title"]
                title = title.strip()
                title = spell_checker.check(title).checked
                tokens = tokenizer.morphs(title)
                data = json.dumps(survey) + SPLITTER+' '.join(tokens)
                print(data)
                o.write(data+'\n')
