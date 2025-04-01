
"""
В данном файле хранятся простейшие функции, выполняющие базовые операции для решения задач лабораторной работы
"""

# Функции для обработки входных данных из файла

def input_graph_t1(file_path):
    file = open(file_path, "r")
    l = [int(x) for x in file.readline().split()]
    ways = []
    ways_2 = []
    for s in file:
        a = [int(x) for x in s.split()]
        ways_2.append(a)
        ways.append((a[0], a[1]))
    return l[0], l[1], ways, ways_2





# Функции для проверки входных данных

def check_graphs_t1(n, m, w2):
    if not(2 <= int(n) <= 10**3):
        return False
    if not(1 <= int(m) <= 10**3):
        return False

    for i in range(len(w2)):








