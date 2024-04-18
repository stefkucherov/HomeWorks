# num1 = (input("Введите первое число: "))
# num2 = (input("Введите второе число: "))
#
# if not (num1.isdigit() and num2.isdigit()):
#     print("Пожалуйста, введите числа!")
#     exit()
# #
# # num1 = float(num1)
# # num2 = float(num2)
# #
# # operation = input("Выберите операцию (+ ,- ,/ ,* ) ")
# #
# # if operation == "+":
# #     result = num1 + num2
# # elif operation == "-":
# #     result = num1 - num2
# #
# # if operation == "*":
# #     result = num1 * num2
# # elif operation == "/":
# #     result = num1 / num2
# #
# # print("Результат: ",result)


#Пример первый

# import math
#
# a = float(input("Введите значение переменной a: "))
# b = float(input("Введите значение переменной b: "))
#
# y= (a**2/3)+(a**2+4/b)+(math.sqrt((a**2+4)/4))+(math.sqrt(a**2+4)**3)/4
# print(y)

# Пример второй

# import math
#
# x = float(input("Введите значение переменной x: "))
#
# y = math.cos(x) + math.sin(x)
# print(y)

# Пример третий
# import math
#
# x = float(input("Введите значение переменной x: "))
#
# y = (math.cos(x**2)**2 + math.sin(2*x - 1)**2)**1/3
# print(y)

# Пример четвертый
#
# import math
#
# x = float(input("Введите значение переменной x: "))
#
# y = 5*x + 3*x**2 * math.sqrt(1 + math.sin(x)**2)
# print(y)

# "Кредитнулся-проиграл"

# i = float(input("Введите годовую процентную ставку: "))
# s = float(input("Введите сумму займа: "))
# n = float(input("Введите количество месяцев на которые взят кредит: "))
# p = i/12
# m = (s*p*(1+p)**n)/(1+p)**n-1
# print(m)

# import math
#
# r = float(input("Введите радиус орбиты планеты: "))
# v = float(input("Введите орбитальную скорость: "))
#
# L = 2*r*math.pi/v
#
# print("Длина года на вашей планете составляет ",L)
