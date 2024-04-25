import random


def create_matrix(lines, colums):
    matrix = []
    for i in range(lines):
        row = []
    for j in range(colums):
        row.append(random.randint(a=1, b=100))
    matrix.append(row)
    return matrix


def check_columns(matrix, H):
    num_columns = len(matrix[0])
    result = []

    for j in range(num_columns):
        has_H = any(matrix[i][j] == H for i in range(len(matrix)))
        result.append(has_H)

    return result


# Создаем случайную матрицу M x N (здесь можно использовать вашу матрицу)
matrix = create_matrix(lines=4, colums=4)

print(matrix)
H = int(input('Введите искомое число: '))

# Проверяем столбцы на наличие числа H
column_results = check_columns(matrix, H)

# Выводим результаты
for j, has_H in enumerate(column_results):
    if has_H:
        print(f"Столбец {j + 1} имеет число {H}")
    else:
        print(f"Столбец {j + 1} не имеет числа {H}")
