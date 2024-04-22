import random
def create_random_matrix(lines, columns):
    matrix = []  # Создаем пустой список, который будет представлять собой матрицу
    for i in range(lines):  # Проходим по каждой строке
        row = []  # Создаем пустой список для текущей строки
        for j in range(columns):  # Проходим по каждому столбцу в текущей строке
            row.append(random.randint(1, 100))  # Добавляем в текущую строку случайное число от 1 до 100
        matrix.append(row)  # Добавляем текущую строку в матрицу
    return matrix


# Пример использования функции для создания матрицы 3x4
matrix = create_random_matrix(3, 4)
print(matrix)
