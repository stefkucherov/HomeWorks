try:
    weight = float(input("Введите ваш вес (кг): "))
    height = float(input("Введите ваш рост (см): "))
    imt = weight / (height / 100) ** 2

    if imt < 18.5:
        print("Недовес")
    elif 18.5 <= imt < 25:
        print("Норма")
    elif 25 <= imt < 30:
        print("Избыточный вес")
    else:
        print("Ожирение")

except ValueError:
    print("Ошибка: Введите корректные числа для веса и роста.")
