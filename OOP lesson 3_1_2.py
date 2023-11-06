"""ЗАДАЧА № 1 и ЗАДАЧА № 2 c подключением библиотеки collections"""

import json
import collections


def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open(file_path, 'r', encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        description = []
        popular_words = []
        for item in news['rss']['channel']['items']:
            for word in item['description'].split(' '):
                if len(word) > word_max_len:
                    description.append(word)
        description_words.extend(description)
        words_counter = collections.Counter(description_words)
        for w in words_counter.most_common(top_words_amt):
            popular_words.append(w[0])
        return popular_words


if __name__ == '__main__':
    print(read_json('newsafr.json'))


import collections
import xml.etree.ElementTree as ET


def read_xml(file, len_word=6, top_words=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file, parser)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    description_words = []
    descriptions = []
    popular_words = []
    for item in xml_items:
        descriptions.append(item.find('description').text.split())
    description = []
    for description in descriptions:
        description = [word for word in description if len(word) > len_word]
        description_words.extend(description)
    words_counter = collections.Counter(description_words)
    for w in words_counter.most_common(top_words):
        popular_words.append(w[0])
    return popular_words


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))
