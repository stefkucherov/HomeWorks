def calculate_statistics(numbers):
    if not numbers:
        return None, None, None

    total_sum = sum(numbers)
    min_number = min(numbers)
    max_number = max(numbers)

    return total_sum, min_number, max_number


numbers = []
n = int(input("Введите количество чисел в списке: "))
print("Введите числа по одному:")

for _ in range(n):
    number = float(input())
    numbers.append(number)

sum_result, min_result, max_result = calculate_statistics(numbers)

print("Сумма всех чисел:", sum_result)
print("Минимальное число:", min_result)
print("Максимальное число:", max_result)