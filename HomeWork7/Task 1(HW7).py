# Работа с модулем os
import os
import shutil


def create_folders():
    # Создаем общую папку FirstFolder (если не существует)
    current_dir = os.getcwd()
    first_folder = os.path.join(current_dir, 'FirstFolder')
    os.makedirs(first_folder, exist_ok=True)
    return first_folder


def create_all_folder():
    # Создаем папку all, где будут лежать все файлы для сортировки
    first_folder = create_folders()
    all_folder = os.path.join(first_folder, 'all')
    os.makedirs(all_folder, exist_ok=True)
    return all_folder


def check_files_in_all_folder():
    # Проверяем наличие файлов в папке all
    all_folder = create_all_folder()
    files = os.listdir(all_folder)
    return len(files)


def calculate_total_size():
    # Вычисляем суммарный размер файлов в папке all
    all_folder = create_all_folder()
    files = os.listdir(all_folder)
    total_size = sum(os.path.getsize(os.path.join(all_folder, file)) for file in files)
    return total_size


def sort_files():
    # Сортируем jpg и txt файлы по папкам jpg_files или txt_files
    all_folder = create_all_folder()
    txt_folder = os.path.join(create_folders(), 'txt_files')
    jpg_folder = os.path.join(create_folders(), 'jpg_files')
    os.makedirs(txt_folder, exist_ok=True)
    os.makedirs(jpg_folder, exist_ok=True)

    files = os.listdir(all_folder)
    txt_count = 0
    jpg_count = 0
    for file in files:
        if file.endswith('.txt'):
            shutil.move(os.path.join(all_folder, file), os.path.join(txt_folder, file))
            txt_count += 1
        elif file.endswith('.jpg'):
            shutil.move(os.path.join(all_folder, file), os.path.join(jpg_folder, file))
            jpg_count += 1

    return txt_count, jpg_count


def main():
    # Основная функция, выполняющая все действия
    txt_count, jpg_count = sort_files()
    total_size = calculate_total_size()

    print(f'В папке с текстовыми файлами перемещено {txt_count} файлов')
    print(f'В папке с изображениями перемещено {jpg_count} файлов.')
    print(f"Их суммарный размер – {total_size}")
    print(f"Имя операционной системы: {os.name}")


if __name__ == "__main__":
    main()
