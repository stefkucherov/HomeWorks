number = int(input("Введите число: "))
hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10
print('Сумма цифр вашего числа равна =',hundreds+tens+ones)