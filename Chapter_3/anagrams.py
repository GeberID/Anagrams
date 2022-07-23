import sys
from pprint import pprint

def load_dict (list:list) -> list:
    try:
        with open(list) as words:
            word_list = words.read().split('\n')
        return word_list
    except Exception as err:
        print("Error ",err)
        sys.exit(1)


def search_anagrams(list:list) -> list:
    users_word = input('Write your word ')
    users_word = users_word.lower()
    users_word_list = sorted(str(users_word))
    anagrams = [i for i in list if users_word_list == sorted(i.lower()) and i != users_word]
    return anagrams

test = load_dict('words_2.txt')
anagrams = search_anagrams(test)
pprint(anagrams)
