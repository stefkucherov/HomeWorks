import math
x = float(input("Введите значение переменной x: "))
y = 5 * x + 3 * x ** 2 * math.sqrt(1 + math.sin(x) ** 2)
print(y)
