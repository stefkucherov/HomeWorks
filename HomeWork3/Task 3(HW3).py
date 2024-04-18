def fibonacci(x):
    fib_sequence = [0, 1]  # Начальные два числа Фибоначчи

    if x <= 0:
        return "Пожалуйста, введите число больше 0"
    elif x == 1:
        return [0]
    elif x == 2:
        return [0, 1]
    else:
        for _ in range(2, x):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Добавляем следующее число Фибоначчи
        return fib_sequence


x = int(input("Введите количество чисел Фибоначчи: "))
print(fibonacci(x))