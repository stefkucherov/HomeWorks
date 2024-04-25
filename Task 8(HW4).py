import random


def create_matrix(lines, colums):
    matrix = []
    for i in range(lines):
        row = []
    for j in range(colums):
        row.append(random.randint(a=1, b=100))
    matrix.append(row)
    return matrix


def calculate_column_sums(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if num_rows > 0 else 0

    column_sums = [0] * num_columns

    for row in matrix:
        for j in range(num_columns):
            column_sums[j] += row[j]

    return column_sums


def calculate_column_percentages(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if num_rows > 0 else 0

    column_sums = calculate_column_sums(matrix)
    total_sum = sum(column_sums)

    column_percentages = [(col_sum / total_sum) * 100 for col_sum in column_sums]
    return column_percentages


# Пример использования:
random_matrix = create_matrix(3, 3)
column_percentages = calculate_column_percentages(random_matrix)

for i, col_percentage in enumerate(column_percentages):
    print(f"Процент суммы в столбце {i + 1}: {col_percentage:.2f}%")