def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Если элемент не найден


arr = list(map(int, input("Введите отсортированный список чисел через пробел: ").split()))

target = int(input("Введите значение, которое нужно найти: "))

# Выполнение бинарного поиска
result = binary_search(arr, target)
if result != -1:
    print(f"Элемент {target} найден в позиции {result}.")
else:
    print("Элемент не найден.")
