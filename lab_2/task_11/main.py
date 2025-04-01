from lab_2.utils import input_data_t11, check_input_data_t11, output_data_t6


def balanced_binary_tree(operation_list):
    """
    Выполняет операции над набором чисел.

    Параметры:
        operation_list (list[str]): Список строк, представляющий последовательность операций и их аргументов.
                                    Операции и соответствующие числа располагаются последовательно. Например:
                                    ["insert", "5", "delete", "3", "exists", "5", "next", "2", "prev", "5"].
    Возвращаемое значение:
        str: Результирующая строка, содержащая результаты операций "exists", "next" и "prev". Результаты каждой
             операции записываются в отдельной строке. Если соответствующий элемент не найден, то возвращается строка "none".

    Пример:
        >>> operations = ["insert", "5", "insert", "3", "exists", "3", "next", "3", "prev", "5"]
        >>> print(balanced_binary_tree(operations))
        true
        5
        3
    """
    num_plenty = set()
    true, false = 'true', 'false'
    nums_more_x, nums_less_x = [], []
    operations_with_nums = ['insert', 'delete', 'exists', 'next', 'prev']
    result_string = ''
    for i in range(len(operation_list) - 1):
        if operation_list[i] == operations_with_nums[0]:
            num_plenty.add(int(operation_list[i + 1]))
        if operation_list[i] == operations_with_nums[1]:
            num_plenty.remove(int(operation_list[i + 1]))
        if operation_list[i] == operations_with_nums[2]:
            if int(operation_list[i + 1]) in num_plenty:
                result_string += true
                result_string += '\n'
            else:
                result_string += false
                result_string += '\n'
        if operation_list[i] == operations_with_nums[3]:
            for bigger in num_plenty:
                if bigger > int(operation_list[i + 1]):
                    nums_more_x.append(bigger)
            min_n_more_x = str(min(nums_more_x))
            if int(min_n_more_x) in num_plenty:
                result_string += min_n_more_x
                result_string += '\n'
            else:
                result_string += 'none'
                result_string += '\n'
        if operation_list[i] == operations_with_nums[4]:
            for smaller in num_plenty:
                if smaller < int(operation_list[i + 1]):
                    nums_less_x.append(smaller)
            max_n_less_x = str(max(nums_less_x))
            if int(max_n_less_x) in num_plenty:
                result_string += max_n_less_x
                result_string += '\n'
            else:
                result_string += 'none'
                result_string += '\n'
    return result_string



if __name__=="__main__":
    FILE_INPUT = './txtf/input.txt'
    FILE_OUTPUT = './txtf/output.txt'
    operations = input_data_t11(FILE_INPUT)
    check = check_input_data_t11(operations)
    if check:
        result = balanced_binary_tree(operations)
        output_data_t6(FILE_OUTPUT, str(result))
    else:
        raise ValueError('ОШИБКА ВХОДНЫХ ДАННЫХ')

