text = input("Введите строку ")
print("Третий символ строки:", text[2])
print("Предпоследний символ строки:", text[-2])
print("Первые пять символов строки:", text[:5])
print("Вся строка до последних двух символов:", text[:-2])
print("Символы с четными индексами:", text[::2])
print("Символы с нечетными индексами:", text[1::2])
print("Все символы в обратном порядке:", text[::-1])
print("Все символы через один в обратном порядке:", text[::-2])
print("Длина строки:", len(text))
