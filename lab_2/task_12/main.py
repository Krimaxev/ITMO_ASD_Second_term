from lab_2.utils import input_data_t12, output_data_t12


def balance_binary_tree(data):
    """
    Вычисляет баланс узлов двоичного дерева на основе заданного представления.

    Функция принимает список целых чисел, в котором первое число n задаёт количество узлов дерева.
    Далее следуют описания узлов в виде троек чисел: k, l, r, где:
      - k: значение или ключ узла (не используется при вычислении высот),
      - l: индекс левого ребенка (0, если отсутствует),
      - r: индекс правого ребенка (0, если отсутствует).

    Пример:
        >>> data = [3, 10, 2, 3, 20, 0, 0, 30, 0, 0]
        >>> balance_binary_tree(data)
        [0, 0, 0]
    """
    index = 0
    n = data[index]
    index += 1
    nodes = [(0, 0)] * (n + 1)
    heights = [0] * (n + 1)
    balances = []

    if n == 0:
        return []

    for i in range(1, n + 1):
        k, l, r = data[index], data[index + 1], data[index + 2]
        nodes[i] = (l, r)
        index += 3

    for i in range(n, 0, -1):
        left, right = nodes[i]
        left_h = heights[left] if left != 0 else -1
        right_h = heights[right] if right != 0 else -1
        heights[i] = 1 + max(left_h, right_h)

    for i in range(1, n + 1):
        left, right = nodes[i]
        left_h = heights[left] if left != 0 else -1
        right_h = heights[right] if right != 0 else -1
        balances.append(right_h - left_h)

    return balances


if __name__ == "__main__":
    FILE_INPUT = './txtf/input.txt'
    FILE_OUTPUT = './txtf/output.txt'
    data = input_data_t12(FILE_INPUT)
    result = balance_binary_tree(data)
    output_data_t12(FILE_OUTPUT, result)
