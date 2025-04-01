from lab_1.utils import open_file_t6, write_file, check_input_values_t6


def largest_number(numbers):
    """
    Формирует наибольшее возможное число путем объединения элементов списка.
    Параметры:
        numbers (list[int]): Список неотрицательных чисел, которые необходимо объединить в наибольшее число.

    Возвращаемое значение:
        str: Строковое представление наибольшего возможного числа – наибольшей возможной зарплаты)

    Пример:
        >>> largest_number([50, 2, 1, 9])
        '95021'
    """
    numbers = list(map(str, numbers))
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] + numbers[j + 1] < numbers[j + 1] + numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return ''.join(numbers)



if __name__=="__main__":
    FILE_INPUT = './txtf/input.txt'
    FILE_OUTPUT = './txtf/output.txt'
    input_nums = open_file_t6(FILE_INPUT)
    cnt_nums, nums = input_nums[0], input_nums[1]
    check = check_input_values_t6(cnt_nums, nums)
    if check:
        result = largest_number(nums)
        write_file(FILE_OUTPUT, result)
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
