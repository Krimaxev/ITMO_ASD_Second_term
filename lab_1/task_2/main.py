from lab_1.utils import open_file_t2, write_file, check_input_values_t2


def min_refills(d, m, n, stops):
    """
    Определяет минимальное число заправок, необходимых для достижения пункта назначения.

    Параметры:
        d (int): Расстояние до пункта назначения (в километрах).
        m (int): Максимальное расстояние, которое автомобиль может проехать без дозаправки.
        n (int): Количество остановок для дозаправки.
        stops (list[int]): Список расстояний (в километрах) от начальной точки до каждой остановки для дозаправки.
                           Список должен быть отсортирован по возрастанию.

    Возвращаемое значение:
        int: Минимальное количество дозаправок, необходимых для достижения пункта назначения. Если достижение
             пункта назначения невозможно, возвращает -1.

    Пример:
        >>> min_refills(950, 400, 4, [200, 375, 550, 750])
        2
    """
    num_refills = 0
    current_position = 0
    last_refill_position = 0
    max_reach = m
    i = 0

    while max_reach < d:
        while i < n and stops[i] <= max_reach:
            last_refill_position = stops[i]
            i += 1

        if last_refill_position == current_position:
            return -1

        num_refills += 1
        current_position = last_refill_position
        max_reach = current_position + m

    return num_refills


if __name__ == "__main__":
    FILE_INPUT = "./txtf/input.txt"
    FILE_OUTPUT = "./txtf/output.txt"
    input_values = open_file_t2(FILE_INPUT)
    distance, fuel_volume, num_fuel_stations, stops = input_values[0], input_values[1], input_values[2], input_values[3]
    check = check_input_values_t2(distance, fuel_volume, num_fuel_stations, stops)
    if check:
        result = min_refills(distance, fuel_volume, num_fuel_stations, stops)
        write_file(FILE_OUTPUT, result)
    else:
        write_file(FILE_OUTPUT, "ОШИБКА ВХОДНЫХ ДАННЫХ")
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
