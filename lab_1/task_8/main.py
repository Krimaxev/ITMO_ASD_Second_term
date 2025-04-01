from lab_1.utils import open_file_t8, write_file, check_input_values_t8



def sort_lectures(lectures):
    """
        Сортирует список лекций по времени их окончания с использованием алгоритма сортировки выбором.

        Параметры:
            lectures (list[tuple[int, int]]): Список лекций, где каждая лекция задаётся парой значений,
                                               представляющих время начала и время окончания.
        Возвращаемое значение:
            list[tuple[int, int]]: Новый отсортированный список лекций по возрастанию времени окончания.

        Пример:
            >>> lectures = [(1, 3), (2, 5), (0, 2)]
            >>> sort_lectures(lectures)
            [(0, 2), (1, 3), (2, 5)]
        """
    n = len(lectures)
    for i in range(n):
        min_elem = i
        for j in range(i + 1, n):
            if lectures[j][1] <= lectures[min_elem][1]:
                min_elem = j
        lectures[i], lectures[min_elem] = lectures[min_elem], lectures[i]
    return lectures



def max_lectures(asks, lectures):
    """
        Определяет максимальное количество лекций, основываясь на их расписании.

        Параметры:
            asks (int): Задает особые условия для результата.
            lectures (list[tuple[int, int]]): Список лекций, где каждая лекция представлена кортежем (время начала, время окончания),
                                               указывающим время начала и окончания лекции.

        Возвращаемое значение:
            int: Максимальное число выполнения заявок на лекции.

        Пример:
            >>> lectures = [(1, 3), (3, 5), (5, 7)]
            >>> max_lectures(2, lectures)
            3
        """
    lectures = sort_lectures(lectures)
    if asks == 0:
        return 0
    if asks == 1:
        return 1
    else:
        count = 1
        for i in range(len(lectures)-1):
            if lectures[i][1] <= lectures[i+1][0]:
                count += 1
    return count



if __name__=="__main__":
    FILE_INPUT = "./txtf/input.txt"
    FILE_OUTPUT = "./txtf/output.txt"
    input_lectures = open_file_t8(FILE_INPUT)
    print(input_lectures)
    asks, times = input_lectures[0], input_lectures[1]
    check = check_input_values_t8(asks, times)
    if check:
        result = max_lectures(asks, times)
        write_file(FILE_OUTPUT, result)
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")