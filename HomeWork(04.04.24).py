# # Task 2
# import math
# cat1 = float(input("Введите первый катет: "))
# cat2 = float(input("Введите второй катет: "))
# hypotenuse = math.sqrt(cat1**2 + cat2**2)
# print("Гипотенуза равна", hypotenuse)
#
# # Task 3
# text = input("Введите текст: ")
# words = text.split()
# print("Количество слов в данной строке =", len(words))
#
# # Task 4
# original_text = input("Напишите текст: ")
# new_text = original_text.replace("h", "H")
# print("Реформат строки:", new_text)
#
# # Task 5
# text = input("Введите строку ")
# print("Третий символ строки:", text[2])
# print("Предпоследний символ строки:", text[-2])
# print("Первые пять символов строки:", text[:5])
# print("Вся строка до последних двух символов:", text[:-2])
# print("Символы с четными индексами:", text[::2])
# print("Символы с нечетными индексами:", text[1::2])
# print("Все символы в обратном порядке:", text[::-1])
# print("Все символы через один в обратном порядке:", text[::-2])
# print("Длина строки:", len(text))
#
# # Task 6
# number = int(input("Введите число: "))
# print('Последняя цифра вашего числа =', number % 10)
#
# # Task 7
# number = int(input("Введите число: "))
# print('Количество десятков в вашем числе =', (number % 100)//10)
#
# # Task 8
# number = int(input("Введите число: "))
# hundreds = number // 100
# tens = (number % 100) // 10
# ones = number % 10
# print('Сумма цифр вашего числа равна =',hundreds+tens+ones)
