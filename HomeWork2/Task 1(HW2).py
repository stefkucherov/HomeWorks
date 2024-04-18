import math

a = float(input("Введите значение переменной a: "))
b = float(input("Введите значение переменной b: "))

y = (a**2/3)+(a**2+4/b)+(math.sqrt((a**2+4)/4))+(math.sqrt(a**2+4)**3)/4
print(y)
