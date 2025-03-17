from lab_2.utils import input_data_t10, check_input_data_t10, output_data_t6


def bst(n, nodes):
    """
    Проверяет, является ли дерево двоичным деревом поиска (BST).

    :param N: Количество вершин в дереве.
    :param nodes: Список описаний вершин.
    :return: True, если дерево является BST, иначе False.
    """
    if n == 0:
        return True
    stack = [(1, float('-inf'), float('inf'))]
    while stack:
        node_idx, min_val, max_val = stack.pop()
        k, l, r = nodes[node_idx]
        if k <= min_val or k >= max_val:
            return False
        if l != 0:
            stack.append((l, min_val, k))
        if r != 0:
            stack.append((r, k, max_val))
    return True


if __name__ == "__main__":
    FILE_INPUT = './txtf/input.txt'
    FILE_OUTPUT = './txtf/output.txt'

    input_f = input_data_t10(FILE_INPUT)
    num,  nodes = input_f[0], input_f[1]

    if num == 0:
        output_data_t6(FILE_OUTPUT, 'YES')
    else:
        check = check_input_data_t10(FILE_INPUT)
        if check:
            result = is_bst(num, nodes)
            if result:
                output_data_t6(FILE_OUTPUT, 'YES')
            else:
                output_data_t6(FILE_OUTPUT, 'NO')
        else:
            raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
