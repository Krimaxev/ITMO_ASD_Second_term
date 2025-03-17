from lab_2.utils import input_data_t6, check_input_data_t6, output_data_t6


def tree_lines(values):
    """
    Преобразует список строк в список узлов дерева.

    Параметры:
        values (list[str]): Список строк, каждая из которых содержит три целых числа, разделённых пробелами.

    Возвращаемое значение:
        list[tuple[int, int, int]]: Список c вложенными списками, представляющими собой узлы дерева. Каждый подсписок имеет три элемента:
                                     ключ узла, индекс левого ребёнка и индекс правого ребёнка.
    Пример:
        >>> input_lines = ["4 1 2", "2 -1 -1", "5 -1 -1"]
        >>> tree_lines(input_lines)
        [[4, 1, 2], [2, -1, -1], [5, -1, -1]]
    """
    results = []
    for i in range(len(values)):
        s = values[i]
        m = [int(x) for x in s.split()]
        k_v, l_v, r_v = m[0], m[1], m[2]
        results.append([k_v, l_v, r_v])
    return results


def is_binary_search_tree(nodes):
    """
    Проверяет, является ли заданное двоичное дерево корректным бинарным деревом поиска (BST).

    Параметры:
        nodes (list[tuple[int, int, int]]): Список узлов дерева.

    Возвращаемое значение:
        bool: истина, если дерево удовлетворяет условиям бинарного дерева поиска, иначе ложь.

    Пример:
        >>> nodes = [[4, 1, 2], [2, -1, -1], [5, -1, -1]]
        >>> is_binary_search_tree(nodes)
        True
    """
    if not nodes:
        return True

    def check_node(idx, min_val=float('-inf'), max_val=float('inf')):
        if idx == -1:
            return True

        key, left, right = nodes[idx]
        if key <= min_val or key >= max_val:
            return False

        left_ok = check_node(left, min_val, key)
        right_ok = check_node(right, key, max_val)

        return left_ok and right_ok

    return check_node(0)



if __name__ == "__main__":
    FILE_INPUT = './txtf/input.txt'
    FILE_OUTPUT = './txtf/output.txt'

    input_values = input_data_t6(FILE_INPUT)
    all_klr = tree_lines(input_values[1])
    n = input_values[0]
    if n==0:
        output_data_t6(FILE_OUTPUT, "CORRECT")
    else:
        k, l, r = all_klr[0]

        check = check_input_data_t6(n, k, l, r, input_values[1])
        if check:
            if is_binary_search_tree(all_klr):
                result = "CORRECT"
            else:
                result = "INCORRECT"
                output_data_t6(FILE_OUTPUT, result)
        else:
            raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")