from hanspell import spell_checker
from konlpy.tag import Kkma
import json

tokenizer = Kkma()


def normalize(key):
    key = key.strip()
    key = spell_checker.check(key).checked
    key = tokenizer.morphs(key)
    return ' '.join(key)


def initialize():
    tokenized_list = []

    with open('surveys.json', 'r', encoding='utf-8') as f:
        json_text = f.read()
        object_list = json.loads(json_text)
        for obj in object_list:
            key = obj["title"]
            tokens = normalize(key)
            data = {
                'tokens': tokens,
                'object': obj
            }
            tokenized_list.append(data)

    with open('parsed.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tokenized_list))
