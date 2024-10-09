import csv
import sys
import math

def calculate_entropy(relationships, n):
    k = len(relationships[0])  # Количество отношений (столбцов)
    entropy = 0
    for i in range(n):
        for j in range(k):
            l_ij = relationships[i][j]
            if l_ij > 0:
                entropy -= (l_ij / (n - 1)) * math.log(l_ij / (n - 1), 2)
    return round(entropy, 1)

def main(file_path: str) -> str:
    relationships = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        relationships = [[int(value) for value in row] for row in reader]

    n = len(relationships)  # Количество узлов

    entropy = calculate_entropy(relationships, n)

    print(entropy)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task.py <путь к файлу>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

