import json
import numpy as np

# Чтение JSON
with open('graph.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Получаем список узлов
nodes = data['nodes']
node_keys = list(nodes.keys())
num_nodes = len(node_keys)

# Создание матрицы смежности
adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

# Заполнение матрицы смежности
for i, node in enumerate(node_keys):
    for neighbor in nodes[node]:
        j = node_keys.index(neighbor)
        adjacency_matrix[i][j] = 1


print("Матрица смежности:")
print(adjacency_matrix)