import os
import re
import sys
from collections import Counter


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath) as infile:
            return infile.read()
    else:
        sys.exit("Неверный путь к файлу или имя файла")


def get_most_frequent_words(filename, number_or_words):
    file_content = load_data(filename)
    all_words_in_file = re.findall(r"[а-яА-ЯA-Za-z]+-?[а-яА-ЯA-Za-z]+", file_content, re.UNICODE)
    all_words_in_file_lower = [word.lower() for word in all_words_in_file]
    counted_words = Counter(all_words_in_file_lower)
    most_common_words = counted_words.most_common()[:number_or_words]
    return most_common_words


def print_frequent_words(data):
    for word, rate in data:
        print("{}: {}".format(word, rate))


if __name__ == '__main__':
    number_or_words_to_print = 10
    filename = sys.argv[1]
    frequent_words = get_most_frequent_words(filename, number_or_words_to_print)
    print_frequent_words(frequent_words)
