def evclid_algo(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print('Наибольший делитель заданных значений равен =', evclid_algo(num1, num2))
