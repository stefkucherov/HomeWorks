def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):  # Перебираем все числа от 2 до (number - 1)
        if number % i == 0:     # Если число делится нацело на какое-либо число из диапазона, оно не простое
            return False
    return True

# Пример использования
number = int(input("Введите число: "))
if is_prime(number):
    print(f"{number} - простое число")
else:
    print(f"{number} - не простое число")
