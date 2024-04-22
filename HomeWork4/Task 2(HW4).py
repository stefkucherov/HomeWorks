def numtobin(n):
    if n == 0:
        return ''
    else:
        return numtobin(n // 2) + str(n % 2)


number = int(input('Введите число для перевода в двоичную систему счисления: '))
binary_number = numtobin(number)
print(f"Число {number} в двоичной системе равно {binary_number}")


