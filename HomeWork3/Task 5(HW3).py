def check_uniqueness(numbers):
    duplicates = {}

    for num in numbers:
        duplicates[num] = duplicates.get(num, 0) + 1

    duplicates = {num: count for num, count in duplicates.items() if count > 1}

    if duplicates:
        print("Некоторые элементы не уникальны:")
        for num, count in duplicates.items():
            print(f"Число {num} повторяется {count} раз(а).")
    else:
        print("Все элементы в списке уникальны.")


input_numbers = input("Введите числа через пробел: ")
numbers = list(map(int, input_numbers.split()))
check_uniqueness(numbers)
