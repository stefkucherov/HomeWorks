strings = ["abcсba", "hello", "level", "python", "madam", "racecar"]


def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Приводим к нижнему регистру и удаляем пробелы
    return s == s[::-1]  # Сравниваем строку с её обратным порядком


p_word = list(filter(is_palindrome, strings))
print('Cлова палиндромы это ', p_word)
