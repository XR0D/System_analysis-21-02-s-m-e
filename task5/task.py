import numpy as np
import json

def read_json(file_path):
    """Считываем JSON файл и возвращаем данные под ключом 'data'."""
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['data']

def write_json(data, file_path):
    """Записываем данные в JSON файл."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def build_relation_matrix(ranking, size):
    """Создаем матрицу отношений на основе ранжировки."""
    matrix = np.zeros((size, size), dtype=int)
    np.fill_diagonal(matrix, 1)

    for idx, group in enumerate(ranking):
        if isinstance(group, int):
            group = [group]

        for i in group:
            for j in group:
                matrix[i - 1][j - 1] = 1

        for i in group:
            for prev_group in ranking[:idx]:
                if isinstance(prev_group, int):
                    prev_group = [prev_group]
                for j in prev_group:
                    matrix[j - 1][i - 1] = 1

    return matrix

def find_discrepancies(matrix_a, matrix_b):
    """Находим противоречия между двумя матрицами отношений."""
    size = matrix_a.shape[0]
    discrepancies = []
    for i in range(size):
        for j in range(size):
            if (matrix_a[i, j] == 1 and matrix_b[i, j] == 0 and
                matrix_a[j, i] == 0 and matrix_b[j, i] == 1):
                discrepancies.append((i + 1, j + 1)) 
            elif (matrix_a[i, j] == 0 and matrix_b[i, j] == 1 and
                  matrix_a[j, i] == 1 and matrix_b[j, i] == 0):
                discrepancies.append((j + 1, i + 1))
    return discrepancies

def find_core(discrepancies):
    """Формируем ядро противоречий из списка противоречий."""
    core = []
    added = set()

    for x, y in discrepancies:
        if any(x in group or y in group for group in core):
            for group in core:
                if x in group or y in group:
                    if x not in group:
                        group.append(x)
                    if y not in group:
                        group.append(y)
                    break
        else:
            core.append([x, y])

        added.update([x, y])

    return core

def main(file_a, file_b, output_file):
    """Основная функция для выполнения программы."""
    ranking_a = read_json(file_a)
    ranking_b = read_json(file_b)

    size_a = sum(len(group) if isinstance(group, list) else 1 for group in ranking_a)
    size_b = sum(len(group) if isinstance(group, list) else 1 for group in ranking_b)
    size = max(size_a, size_b)

    matrix_a = build_relation_matrix(ranking_a, size)
    print("Matrix A:")
    print(matrix_a)

    matrix_b = build_relation_matrix(ranking_b, size)
    print("Matrix B:")
    print(matrix_b)

    discrepancies = find_discrepancies(matrix_a, matrix_b)
    print(f"Discrepancies: {discrepancies}")

    core = find_core(discrepancies)
    print(f"Core: {core}")

    write_json({"core": core}, output_file)

if __name__ == "__main__":
    main("task5/a.json", "task5/b.json", "task5/core.json")