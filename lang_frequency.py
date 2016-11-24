from collections import Counter
import re

def load_data(filepath):
    with open(filepath) as infile:
        return infile.read()


def get_most_frequent_words(text):
    # список всех слов (выражение учитывает английский слова и кириллицу, слова не должны начинаться или заканчиваться c "-")
    word_list_re = re.findall(r"[а-яА-ЯA-Za-z]+-[а-яА-ЯA-Za-z]+|[а-яА-ЯA-Za-z]+", text, re.UNICODE)
    # список всех слов c маленькой буквы
    word_list_re = [word.lower() for word in word_list_re]

    # cоставление списка вида {слово: число (как часто встречается)}
    words_dict_count = Counter(word_list_re)

    # вывод top 10
    for word, num in words_dict_count.most_common()[:10]:
        print("{}: {}".format(word, num))

if __name__ == '__main__':
    print(get_most_frequent_words(load_data('text.txt')))
