from json.decoder import JSONDecodeError
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

    with open('objects.json', 'r', encoding='utf-8') as f:
        json_text = f.read()
        object_list = json.loads(json_text)
        counter = 0
        for obj in object_list:
            try:
                key = obj["title"]
                tokens = normalize(key)
                data = {
                    'tokens': tokens,
                    'object': obj
                }
                tokenized_list.append(data)
                counter += 1
                print(counter, key)
            except UnicodeDecodeError:
                pass
            except JSONDecodeError:
                pass

    print(len(tokenized_list), 'docs are processed.')
    print('Saving results to json file', flush=True)

    json.dump(tokenized_list, open('parsed.json', 'w', encoding='utf-8'))


if __name__ == "__main__":
    initialize()
