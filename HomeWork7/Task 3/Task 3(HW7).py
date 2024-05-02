import re


def create_and_fill_input_file():
    try:
        with open('input.txt', 'w', encoding='utf-8') as file:
            print("Введите текст для файла 'input.txt'. Для окончания ввода используйте пустую строку.")
            while True:
                line = input()
                if line == "":
                    break
                file.write(line + '\n')
        print("Файл 'input.txt' успешно создан и заполнен.")
    except Exception as e:
        print(f"Произошла ошибка при создании файла: {e}")


def find_and_write_most_common_word():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open('output.txt', 'w', encoding='utf-8') as output_file:
            for line in lines:
                words = re.findall(r'\b\w+\b', line.lower())
                word_count = {}
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
                most_common_word, count = max(word_count.items(), key=lambda item: item[1], default=(None, 0))
                output_file.write(
                    f' Самое используемое слово {most_common_word} -использовали {count} раз(-а)\n' if most_common_word
                    else 'Нет слов в строке\n')
        print("Файл 'output.txt' успешно создан.")
    except FileNotFoundError:
        print("Файл 'input.txt' не найден. Убедитесь, что он существует и находится в нужной директории.")
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")


# Вызов функций
create_and_fill_input_file()
find_and_write_most_common_word()
