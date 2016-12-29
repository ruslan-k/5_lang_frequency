import sys
from collections import Counter
import re

def load_data(filepath):
    with open(filepath) as infile:
        return infile.read()


def get_most_frequent_words(filename):
    text = load_data(filename)
    all_words_in_text = re.findall(r"[а-яА-ЯA-Za-z]+-?[а-яА-ЯA-Za-z]+", text, re.UNICODE)
    all_words_in_text_lower = [word.lower() for word in all_words_in_text]
    counted_words = Counter(all_words_in_text_lower)

    return counted_words


def print_frequent_words(data):
    top_10_common_words = data.most_common()[:10]
    for word, rate in top_10_common_words:
        print("{}: {}".format(word, rate))


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        frequent_words = get_most_frequent_words(filename)
        print(print_frequent_words(frequent_words))
    except FileNotFoundError:
        print("Неверный путь к файлу или имя файла")
