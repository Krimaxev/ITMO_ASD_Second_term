"""
В данном файле хранятся функции позволяющие выполнять простые операции:
открытие/запись в файлы, проверка входных значений и другие функции, которые актуальны
абсолютно для всех задач, независимо от их условия.
"""


# Функции для обработки входных данных из входного файла

def input_data_t6(filepath):
    file = open(filepath, "r")
    n = int(file.readline())
    m = file.readlines()
    return n, m


def input_data_t10(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    n = int(lines[0].strip())
    nodes = [None] * (n + 1)
    for i in range(1, n + 1):
        k, l, r = map(int, lines[i].strip().split())
        nodes[i] = (k, l, r)
    return n, nodes


def input_data_t11(file_path):
    file = open(file_path, "r")
    values = file.readlines()
    open_values = []
    for s in values:
        operation = s.split()
        for k in operation:
            open_values.append(k)
    return open_values

def input_data_t12(file_path):
    file = open(file_path, 'r')
    data = list(map(int, file.read().split()))
    return data





# Функции для проверки входных данных

def check_input_data_t6(n, k, l, r, trees):
    if int(n) != len(trees):
        return False
    if not(0 <= int(n) <= 10**5):
        return False
    if not((-2**31) <= int(k) <= (2**31 - 1)):
        return False
    if not(-1 <= int(l) <= (int(n) - 1)):
        return False
    if not(-1 <= int(r) <= (int(n) - 1)):
        return False
    if not(l != -1 or r != -1 or l != r):
        return False
    return True


def check_input_data_t10(file_path):
    f = open(file_path, "r")
    n = f.readline()
    nodes = f.readlines()
    results = []
    for i in range(len(nodes)):
        s = nodes[i]
        m = [int(x) for x in s.split()]
        k_v, l_v, r_v = m[0], m[1], m[2]
        results.append([k_v, l_v, r_v])

    keys = [results[i][0] for i in range(len(results))]

    if not(0 <= int(n) <= 2*5**10):
        return False
    if int(n) != len(keys):
        return False
    for i in range(len(keys)):
        if not(abs(keys[i]) <= 10**9):
            return False
    return True


def check_input_data_t11(lst):
    operations = ['insert', 'delete', 'exists', 'next', 'prev']

    if len(lst) % 2 != 0:
        return False

    for i in range(0, len(lst), 2):
        op = lst[i]
        if op not in operations:
            return False

        try:
            num = int(lst[i + 1])
        except ValueError:
            return False

        if abs(num) > 10 ** 9:
            return False

    return True





# Функции для обработки выходных данных и записи в выходной файл

def output_data_t6(filepath, result):
    file = open(filepath, "w")
    file.write(str(result))

def output_data_t12(filename, balances):
    with open(filename, 'w') as file:
        for balance in balances:
            file.write(f"{balance}\n")



