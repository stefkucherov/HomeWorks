"""
Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
Метод is_repeatance(s), который принимает некоторую строку
и возвращает True или False в зависимости от того, может ли
текущая строка быть получена целым количеством повторов
строки s. Считать, что пустая строка не содержит повторов
• Метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""

class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        return self == s * (len(self) // len(s))

    def is_palindrome(self):
        return self.lower() == self.lower()[::-1]


my_str = SuperStr("abcabcabc")
print(my_str.is_repeatance("abc"))

my_palindrome = SuperStr("level")
print(my_palindrome.is_palindrome())
