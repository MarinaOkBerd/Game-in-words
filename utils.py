import random

import requests

from basic_word import BasicWord

words_JSON = "https://www.jsonkeeper.com/b/MOJW"


def load_words(json_url):
    """
    Получает список слов с внешнего ресурса
    """
    info = requests.get(json_url)
    info_words = info.json()
    return info_words


def load_random_word(json_url):
    """
    Возвращает экземпляр класс BasicWord со случайным словом
    """
    info_words = load_words(json_url)
    random_info_words = random.choice(info_words)
    basic_word = BasicWord(random_info_words["word"], random_info_words["subwords"])
    return basic_word

