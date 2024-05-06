def read_students_from_file(filename, min_grade=3):
    """
    Чтение данных из файла и вывод учащихся с оценкой менее min_grade.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            students = []
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 3:
                    last_name, first_name, grade = parts[0], parts[1], int(parts[2])
                    if grade < min_grade:
                        students.append((last_name, first_name, grade))
            if students:
                print("Учащиеся с оценкой менее трёх баллов:")
                for last_name, first_name, grade in students:
                    print(f"{last_name} {first_name} - {grade}")
            else:
                print("Нет учащихся с оценкой менее трёх баллов.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении данных: {e}")

# Пример использования:
filename = 'students.txt'  # Укажите имя вашего файла
read_students_from_file(filename)
