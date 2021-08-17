"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
в теле функции или снаружи.

"""

lang_dct = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'
            }


def translate(word, some_dict):
    if word in some_dict:
        return some_dict[word]
    else:
        return f'None'


print(translate('five', lang_dct))  # пример
