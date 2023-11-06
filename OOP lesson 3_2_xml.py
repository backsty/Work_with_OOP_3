"""ЗАДАЧА № 2"""
import xml.etree.ElementTree as ET


"""функция для чтения файла с новостями."""


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """Функция для чтения файла с новостями."""
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    xml_title = root.findall("channel/item/description")

    all_text_input = []
    repetitions_of_words = []
    all_text_output = []
    for news in xml_title:
        all_text = news.text
        for description_ in all_text.split():
            all_text_input.append(description_)
    uniq_word = set(list(filter(lambda l: len(l) > word_max_len, all_text_input)))

    for word in uniq_word:
        repetitions_of_words.append(all_text_input.count(word))
    number_of_repetitions_of_words = list(zip(repetitions_of_words, uniq_word))
    number_of_repetitions_of_words.sort(reverse=True, key=lambda f: (f[0], -len(f[1])))

    for i, each_word in enumerate(number_of_repetitions_of_words):
        if i < top_words_amt:
            all_text_output.append(each_word[1])
        else:
            return all_text_output


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))