"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг,
разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?

"""

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):  # создаем ф-ю, задаем арг-ты (кол-во шуток и флаг, разрешающий/запрещающий повторы)
    for i in range(n):
        random_1 = choice(nouns)
        random_2 = choice(adverbs)
        random_3 = choice(adjectives)
        joke = f'{random_1} {random_2} {random_3}'
        print(joke)
        if repeat:
            joke_list = joke.split()
            for noun in nouns:
                for word in joke_list:
                    if noun == word:
                        nouns.remove(noun)
            for adverb in adverbs:
                for word in joke_list:
                    if adverb == word:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for word in joke_list:
                    if adjective == word:
                        adjectives.remove(adjective)


get_jokes(n=3, repeat=True)
