from lab_1.utils import open_file_t16, write_output, check_input_values_t16, string_t16
from itertools import permutations


def min_path(num, matrix):
    """
    Находит минимальный по суммарной дистанции путь обхода городов (задача коммивояжера) и возвращает его.

    Параметры:
        num (int): Количество городов.
        matrix (list[list[int]]): Матрица расстояний размером num x num, где matrix[i][j] обозначает расстояние
                                  от города i до города j.

    Возвращаемое значение:
        tuple:
            - str: Строковое представление минимальной суммарной дистанции маршрута.
            - list[int]: Список номеров городов маршрута, возвращённый в обратном порядке. Нумерация городов начинается
                         с 1 (то есть, к исходным индексам добавляется 1).

    """
    cities = list(range(num))
    all_permutations = permutations(cities[1:])
    m_distance = float('inf')
    best_path = None


    for perm in all_permutations:
        current_distance = 0
        current_city = cities[0]

        for next_city in perm:
            current_distance += matrix[current_city][next_city]
            current_city = next_city

        if current_distance < m_distance:
            m_distance = current_distance
            best_path = list((cities[0],) + perm)

            for i in range(len(best_path)):
                best_path[i] = best_path[i] + 1


    return str(m_distance), best_path[::-1]



if __name__ == "__main__":
    FILE_INPUT = "./txtf/input.txt"
    FILE_OUTPUT = "./txtf/output.txt"
    f_input = open_file_t16(FILE_INPUT)
    n, distances = f_input[0], f_input[1]
    check = check_input_values_t16(n, distances)
    if check:
        result = min_path(n, distances)
        min_distance, path = result[0], result[1]
        write_output(FILE_OUTPUT, min_distance, string_t16(path))
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
