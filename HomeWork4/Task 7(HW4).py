import random


def create_random_matrix(lines, columns):
    matrix = []  # Создаем пустой список, который будет представлять собой матрицу
    for i in range(lines):  # Проходим по каждой строке
        row = []  # Создаем пустой список для текущей строки
        for j in range(columns):  # Проходим по каждому столбцу в текущей строке
            row.append(random.randint(1, 100))  # Добавляем в текущую строку случайное число от 1 до 100
        matrix.append(row)  # Добавляем текущую строку в матрицу
    return matrix


def find_min_max(matrix):
    min_value = max(row[0] for row in matrix)
    max_value = min(row[0] for row in matrix)

    for row in matrix:
        for element in row:
            min_value = min(min_value, element)
            max_value = max(max_value, element)

    return min_value, max_value



matrix = create_random_matrix(3, 4)
minmax = find_min_max(matrix)
print('Матрица рандомных элементов', matrix)
print("Минимальное и максимальнок значение массива", minmax)
