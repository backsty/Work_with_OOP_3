"""ЗАДАЧА № 1"""
import json


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """Функция для чтения файла с новостями."""

    all_text_input = []
    repetitions_of_words = []
    all_text_output = []

    with open(file_path, encoding='utf-8') as file:
        json_data = json.load(file)
    new_json_list = json_data["rss"]["channel"]["items"]

    for news in new_json_list:
        for description_ in news["description"].split():
            all_text_input.append(description_)
    uniq_word = set(list(filter(lambda l: len(l) > word_max_len, all_text_input)))

    for word in uniq_word:
        repetitions_of_words.append(all_text_input.count(word))
    number_of_repetitions_of_words = list(zip(repetitions_of_words, uniq_word))
    number_of_repetitions_of_words.sort(reverse=True, key=lambda f: (f[0], len(f[1])))
    for i, each_word in enumerate(number_of_repetitions_of_words):
        if i < top_words_amt:
            all_text_output.append(each_word[1])
        else:
            return all_text_output


if __name__ == '__main__':
    print(read_json('newsafr.json'))