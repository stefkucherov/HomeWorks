# Task 2
# cost = int(input('Введите стоимость телефона: '))
# dailysum = int(input('Ежедневные карманные деньги: '))
# weeksum = dailysum * 6
# days = cost // dailysum
# week = cost // weeksum
# print(f'Для покупки телефона понадобиться {days} дней или около {week} недель.')

# Task 3
# def fibonacci(x):
#     fib_sequence = [0, 1]  # Начальные два числа Фибоначчи
#
#     if x <= 0:
#         return "Пожалуйста, введите число больше 0"
#     elif x == 1:
#         return [0]
#     elif x == 2:
#         return [0, 1]
#     else:
#         for _ in range(2, x):
#             fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Добавляем следующее число Фибоначчи
#         return fib_sequence
#
#
# x = int(input("Введите количество чисел Фибоначчи: "))
# print(fibonacci(x))

# Task 4

# def calculate_statistics(numbers):
#     if not numbers:
#         return None, None, None
#
#     total_sum = sum(numbers)
#     min_number = min(numbers)
#     max_number = max(numbers)
#
#     return total_sum, min_number, max_number
#
#
# numbers = []
# n = int(input("Введите количество чисел в списке: "))
# print("Введите числа по одному:")
#
# for _ in range(n):
#     number = float(input())
#     numbers.append(number)
#
# sum_result, min_result, max_result = calculate_statistics(numbers)
#
# print("Сумма всех чисел:", sum_result)
# print("Минимальное число:", min_result)
# print("Максимальное число:", max_result)

# Task 5
# def check_uniqueness(numbers):
#     duplicates = {}
#
#     for num in numbers:
#         duplicates[num] = duplicates.get(num, 0) + 1
#
#     duplicates = {num: count for num, count in duplicates.items() if count > 1}
#
#     if duplicates:
#         print("Некоторые элементы не уникальны:")
#         for num, count in duplicates.items():
#             print(f"Число {num} повторяется {count} раз(а).")
#     else:
#         print("Все элементы в списке уникальны.")
#
#
# input_numbers = input("Введите числа через пробел: ")
# numbers = list(map(int, input_numbers.split()))
# check_uniqueness(numbers)

# Task 6

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         mid_val = arr[mid]
#
#         if mid_val == target:
#             return mid
#         elif mid_val < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1  # Если элемент не найден
#
#
# arr = list(map(int, input("Введите отсортированный список чисел через пробел: ").split()))
#
# target = int(input("Введите значение, которое нужно найти: "))
#
# # Выполнение бинарного поиска
# result = binary_search(arr, target)
# if result != -1:
#     print(f"Элемент {target} найден в позиции {result}.")
# else:
#     print("Элемент не найден.")
