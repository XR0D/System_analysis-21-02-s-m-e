import csv
import json
import sys
import os

def get_value_from_csv(csv_file_path, row_number, column_number):
    """Функция для получения значения из CSV файла."""
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{csv_file_path}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    
    if row_number < 1 or row_number > len(data):
        print(f"Ошибка: Строка {row_number} не существует.")
        return

    if column_number < 1 or column_number > len(data[row_number - 1]):
        print(f"Ошибка: Колонка {column_number} не существует в строке {row_number}.")
        return

    cell_value = data[row_number - 1][column_number - 1]
    
    print(f"Значение в строке {row_number}, колонке {column_number}: {cell_value}")


def get_value_from_json(json_file_path, row_number, column_number):
    """Функция для получения значения из JSON файла."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{json_file_path}' не найден.")
        return
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{json_file_path}' не является корректным JSON.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    
    rows = data.get('str', {})
    
    values = []
    for key, value in rows.items():
        if isinstance(value, list):
            values.append(value)
        else:
            values.append([value])

    if row_number < 1 or row_number > len(values):
        print(f"Ошибка: Строка {row_number} не существует.")
        return

    if column_number < 1 or column_number > len(values[row_number - 1]):
        print(f"Ошибка: Колонка {column_number} не существует в строке {row_number}.")
        return

    cell_value = values[row_number - 1][column_number - 1]
    
    print(f"Значение в строке {row_number}, колонке {column_number}: {cell_value}")


def get_file_extension(file_path):
    """Функция для получения расширения файла."""
    return os.path.splitext(file_path)[1].lower()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python task.py <путь к файлу> <номер строки> <номер колонки>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        row_number = int(sys.argv[2])
        column_number = int(sys.argv[3])
    except ValueError:
        print("Ошибка: Номера строки и колонки должны быть целыми числами.")
        sys.exit(1)

    file_extension = get_file_extension(file_path)

    if file_extension == '.csv':
        get_value_from_csv(file_path, row_number, column_number)
    elif file_extension == '.json':
        get_value_from_json(file_path, row_number, column_number)
    else:
        print("Ошибка: Неверный формат файла. Укажите файл с расширением '.csv' или '.json'.")