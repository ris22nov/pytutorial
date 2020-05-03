import json
from string_function import get_close_matches
import itertools

data = json.load(open('data.json'))


def word_list(word=""):
    keys = []
    if word == "":
        out = dict(itertools.islice(data.items(), 10))
        for key in (out.keys()):
            keys.append(key)
    else:
        for key in get_close_matches(word, data):
            keys.append(key)
    return keys


def meaning(word):
    try:
        return data[word]
    except:
        try:
            return data[word.capitalize()]
        except:
            return data[word.upper()]
