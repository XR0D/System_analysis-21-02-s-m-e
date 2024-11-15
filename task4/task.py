import pandas as pd
import numpy as np
from typing import List

def load_data(file_path: str) -> pd.DataFrame:
    """Загружает данные из CSV файла."""
    return pd.read_csv(file_path)

def calculate_joint_probabilities(data: pd.DataFrame) -> pd.DataFrame:
    """Рассчитывает совместные вероятности."""
    total_sum = data.iloc[:, 1:].values.sum()
    return data.iloc[:, 1:] / total_sum

def calculate_marginal_probabilities(joint_prob: pd.DataFrame) -> (np.ndarray, np.ndarray):
    """Рассчитывает маргинальные вероятности для A и B."""
    prob_A = joint_prob.sum(axis=1).values
    prob_B = joint_prob.sum(axis=0).values
    return prob_A, prob_B

def entropy(probabilities: np.ndarray) -> float:
    """Вычисляет энтропию для заданного набора вероятностей."""
    return -np.sum(probabilities * np.log2(probabilities, where=(probabilities > 0)))

def calculate_conditional_entropy(joint_prob: pd.DataFrame, prob_A: np.ndarray) -> float:
    """Рассчитывает условную энтропию события B при условии A."""
    conditional_entropy = np.sum([
        p_a * entropy(joint_prob.iloc[idx, :].values / p_a)
        for idx, p_a in enumerate(prob_A) if p_a > 0
    ])
    return conditional_entropy

def main() -> List[float]:
    # Загружаем данные
    data = load_data('task4\example.csv')
    
    # Рассчитываем вероятности
    joint_prob = calculate_joint_probabilities(data)
    prob_A, prob_B = calculate_marginal_probabilities(joint_prob)

    # Рассчитываем энтропии
    H_AB = entropy(joint_prob.values.flatten())
    H_A = entropy(prob_A)
    H_B = entropy(prob_B)
    
    # Рассчитываем условную энтропию и взаимную информацию
    Ha_B = calculate_conditional_entropy(joint_prob, prob_A)
    I_AB = H_B - Ha_B

    # Возвращаем результаты с округлением до двух знаков после запятой
    return [round(H_AB, 2), round(H_A, 2), round(H_B, 2), round(Ha_B, 2), round(I_AB, 2)]

if __name__ == "__main__":
    result = main()
    print(result)