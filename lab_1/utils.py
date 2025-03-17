"""
В данном файле хранятся функции позволяющие выполнять простые операции:
открытие/запись в файлы, проверка входных значений и другие функции, которые актуальны
абсолютно для всех задач, независимо от их условия.
"""


# Функции для обработки входных данных из входного файла

def open_file_t2(filepath):
    """
    Открывает и обрабатывает входной файл задачи №2
    :param filepath: путь к входному файлу:
    :return входные данные для условия задачи:
    """
    f = open(filepath, "r")
    l1 = int(f.readline())
    l2 = int(f.readline())
    l3 = int(f.readline())
    l4 = [int(x) for x in f.readline().split()]
    return l1, l2, l3, l4

def open_file_t6(filepath):
    """
    Открывает и обрабатывает входной файл задачи №6
    :param filepath: путь к входному файлу:
    :return входные данные для условия задачи:
    """
    f = open(filepath, "r")
    l1 = int(f.readline())
    l2 = [int(x) for x in f.readline().split()]
    return l1, l2

def open_file_t8(filepath):
    """
    Открывает и обрабатывает входной файл задачи №8
    :param filepath: путь к входному файлу:
    :return входные данные для условия задачи:
    """
    f = open(filepath, "r")
    n = int(f.readline())
    lectures = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, lectures

def open_file_t16(filepath):
    """
    Открывает и обрабатывает входной файл задачи №16
    :param filepath: путь к входному файлу:
    :return входные данные для условия задачи:
    """
    file = open(filepath, "r")
    n = int(file.readline())
    distances = [list(map(int, file.readline().split())) for _ in range(n)]
    return n, distances

def open_file_t18(filepath):
    """
    Открывает и обрабатывает входной файл задачи №18
    :param filepath: путь к входному файлу:
    :return входные данные для условия задачи:
    """
    f = open(filepath, "r")
    lines = f.read().splitlines()
    if not lines:
        return 0, []
    n = int(lines[0])
    prices = [int(line) for line in lines[1:n + 1]]
    return n, prices





# Функции для записи в файл

def write_file(filepath, res):
    """
    :param filepath: путь к выходному файлу
    :param res: результат обработки входных данных в соответствии с условием задачи
    :return: запись res в выходной файл
    """
    file = open(filepath, "w")
    file.write(str(res))

def output_answer(min_sum, k1, used_days, filepath):
    """
    Выводит итоговый результат в требуемом формате в выходной файл в задаче 18.
    :param min_sum: минимальная сумма затрат
    :param k1: число оставшихся купонов
    :param used_days: список дней, когда использовался купон
    :param filepath: открытый файл для записи выходных данных
    :return: запись параметров в выходной файл
    """
    f = open(filepath, "w")
    k2 = len(used_days)
    f.write(str(min_sum) + "\n")
    f.write(f"{k1} {k2}\n")
    for day in used_days:
        f.write(str(day) + "\n")

def write_output(filename, min_distance, path):
    with open(filename, 'w') as file:
        file.write(f"{min_distance}\n")
        file.write(" ".join(map(str, path)) + "\n")




# Функции для проверки входных данных

def check_input_values_t2(d, m, n, stops):
    """Функция проверяет корректность входных данных в задаче №2"""
    if not(1 <= int(d) <= 10**5):
        return False
    if not(1 <= int(m) <= 400):
        return False
    if not(1 <= int(n) <= 300):
        return False

    for i in range(len(stops)-1):
        if not(int(stops[i]) < int(stops[i+1])):
            return False

    return True


def check_input_values_t6(c, nums):
    """Функция проверяет корректность входных данных в задаче №6"""
    if not(1 <= int(c) <= 10**2):
        return False
    if int(c) != len(nums):
        return False
    for i in range(len(nums)):
        if not(1 <= nums[i] <= 10**3):
            return False
    return True


def check_input_values_t8(n, times):
    """Функция проверяет корректность входных данных в задаче №8"""
    if not(1 <= int(n) <= 1000):
        return False
    if int(n) != len(times):
        return False
    for i in range(len(times)):
        for j in times[i]:
            if  not(1 <= int(j) <= 1440):
                return False
    return True

def check_input_values_t16(c_n, dist):
    """Функция проверяет корректность входных данных в задаче №16"""
    if not(1 <= int(c_n) <= 13):
        return False
    for i in range(len(dist)):
        for j in range(len(dist[i])):
            if not(0 <= dist[i][j] <= 10**6):
                return False
            if dist[i][j] != dist[j][i]:
                return False
            if dist[i][i] != 0:
                return False
    return True


def check_input_values_t18(n, s):
    """Функция проверяет корректность входных данных в задаче №18"""
    if not(0 <= int(n) <= 100):
        return False
    for i in range(len(s)):
        if not(0 <= int(i) <= int(n)):
            return False
        if not(0 <= int(s[i]) <= 300):
            return False
    return True



# Функции для манипуляций со строками в задачах
def string_t16(m):
    """
    Функция для задачи №16
    :param m: лист с числовыми значениями:
    :return s: трока с числами
    """

    s = ''
    for i in range(len(m)):
        s += str(m[i])
    return s






