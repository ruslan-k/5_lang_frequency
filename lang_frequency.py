

from collections import Counter
import re

def load_data(filepath):
    f = open(filepath)
    return f.read()


def get_most_frequent_words(text):
    text = re.sub(r'\d', '', text)
    text_list = [word.lower() for word in re.findall("\w+-\w+|[\w']+", text)]
    words_dict = Counter(text_list)
    for word, num in words_dict.most_common()[:10]:
        print("{}: {}".format(word, num))

if __name__ == '__main__':
    print(get_most_frequent_words(load_data('text.txt')))
