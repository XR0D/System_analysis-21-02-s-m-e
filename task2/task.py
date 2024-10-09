import csv
import sys

def create_tree(edges, n):
    tree = {i: [] for i in range(1, n + 1)}
    for parent, child in edges:
        tree[parent].append(child)
    return tree

def calculate_relationships(edges, n):
    tree = create_tree(edges, n)
    r1 = [len(tree[node]) for node in range(1, n + 1)]  # Количество потомков
    r2 = [0] * n
    r3 = [0] * n
    r4 = [0] * n
    r5 = [0] * n
    parents = {child: parent for parent, child in edges}

    for child in parents:
        r2[child - 1] = 1  # Устанавливаем количество родителей
        if parents[child] in parents:
            r4[child - 1] = 1  # Если есть дед

    for node in range(1, n + 1):
        r3[node - 1] = sum(len(tree[child]) for child in tree[node])  # Количество внуков
        parent = parents.get(node)
        if parent:
            r5[node - 1] = len(tree[parent]) - 1  # Количество братьев

    return r1, r2, r3, r4, r5

def main(file_path: str, output_file: str = None) -> str:
    edges = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        edges = [(int(row[0]), int(row[1])) for row in reader]

    n = max(max(parent, child) for parent, child in edges)  # Общее количество узлов
    relationships = calculate_relationships(edges, n)

    output_data = '\n'.join(','.join(map(str, relation)) for relation in zip(*relationships))

    if output_file:
        with open(output_file, mode='w', newline='') as file:
            file.write(output_data)
        print(f"Данные успешно записаны в файл: {output_file}")
    else:
        print(output_data)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Использование: python task.py <путь к файлу> [<путь к выходному файлу>]")
        sys.exit(1)

    file_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else None

    main(file_path, output_file)