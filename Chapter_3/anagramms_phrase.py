"""
+ Загрузить файл словаря
+ Принять имя от пользователя
+ Установить предел равным длине имени
+ Создать пустой список для хранения анаграммного словосочетания
+ найти анаграммы по фразе, которые подходят по кол букв
+ вывести их
+выбрать начало анаграмной фразы
+удалить все использованные буквы
повторить поиск пока не будут выполняться условия
вывести составленную фразу
"""

import sys
from collections import Counter
from pprint import pprint
import cProfile


def load_dict (file_words: 'file') -> list:
    """Load words from the file"""
    try:
        with open(file_words,encoding="utf-8") as words:
            word_list = words.read().split('\n')
        return word_list
    except Exception as err:
        print("Error ",err)
        sys.exit(1)

def find_anagrams (words_list:list, users_phrace:str)  ->list:
    """Find anagrams"""
    users_phrace = str(users_phrace.lower().replace(' ',''))
    users_phrace_map = Counter(users_phrace)
    anagrams = []
    for word in words_list:
        phrase = ''
        if len(word) <= len(users_phrace) and len(word) > 1:
            word_map = Counter(word)
            for letter in word:
                if word_map[letter] <= users_phrace_map[letter]:
                    phrase+=letter
                if Counter(phrase) == word_map:
                    anagrams.append(word)
    print("Find anagrams:")
    pprint(anagrams)
    return anagrams


def delete_used_letters(users_phrase:str,anagram:str) -> str:
    """Delete letters from the used phrase"""
    users_phrase_map = Counter(users_phrase)
    anagram_map = Counter(anagram)
    optim_phrase = ''
    for letter in anagram_map:
        users_phrase_map[letter] = users_phrase_map[letter] - anagram_map[letter]
        if users_phrase_map[letter] <=0:
            users_phrase_map.pop(letter)
    for i in users_phrase_map:
        optim_phrase+=i*users_phrase_map[i]
    return optim_phrase


def process_choice (words_list:list) ->str:
    """Main func, that use another funcs for search anagrams in phrase"""
    created_anagram_phrase = ""
    print("""Select options:
    Write one of found anagram or write EXIT! to exit from the program
    If program can't find anagrams, program will be only display find anagram phrase""")
    selected_word = input("Write your phrase ")
    selected_word = selected_word.replace(' ','')

    anagrams = find_anagrams(words_list=words_list, users_phrace=selected_word)
    while len(anagrams) != 0:
        choose_anagram = input("Write your anagram ")
        created_anagram_phrase += choose_anagram+" "
        selected_word = delete_used_letters(users_phrase=selected_word.lower(),
                                                               anagram=choose_anagram.lower())
        anagrams = find_anagrams(words_list=words_list, users_phrace=delete_used_letters(
            users_phrase=selected_word,anagram=choose_anagram.lower()))
    print("Your result ",created_anagram_phrase)


test = load_dict('100000-russian-words.txt')
#process_choice(words_list=test)

cProfile.run("find_anagrams(words_list=test,users_phrace='Мама ехала домой на велосипеде')")