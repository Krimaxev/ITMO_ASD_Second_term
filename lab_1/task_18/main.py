from lab_1.utils import open_file_t18, output_answer, check_input_values_t18

def initialize_dp_tables(n, max_k):
    """
    Инициализирует таблицы dp и prev.
    dp[i][k]  – минимальная сумма, которую нужно заплатить
                за первые i товаров, имея k купонов перед покупкой i-го товара.
    prev[i][k] – хранит кортеж (k_previous, is_used), показывающий:
                 предыдущая позиция по купонам k_previous
                 и индикатор использования купона (True/False).
    """
    INF = float('inf')
    dp = [[INF] * (max_k + 2) for _ in range(n + 1)]
    prev = [[None] * (max_k + 2) for _ in range(n + 1)]
    dp[0][0] = 0
    return dp, prev


def process_purchase(i, k_prev, price, dp, prev, max_k):
    """
    Обрабатывает вариант покупки i-го товара за полную стоимость:
    при этом, если price > 100, начисляем купон.
    """
    INF = float('inf')
    if dp[i - 1][k_prev] == INF:
        return

    # Начисляем купон, если цена > 100
    new_k = k_prev + (1 if price > 100 else 0)
    if new_k <= max_k:
        new_sum = dp[i - 1][k_prev] + price
        if new_sum < dp[i][new_k]:
            dp[i][new_k] = new_sum
            prev[i][new_k] = (k_prev, False)


def process_coupon_usage(i, k_prev, dp, prev):
    """
    Обрабатывает вариант покупки i-го товара через использование уже имеющегося купона.
    """
    INF = float('inf')
    # Если нет купона, выходим
    if k_prev < 1 or dp[i - 1][k_prev] == INF:
        return

    # Используем купон, не платим, уменьшаем счётчик купонов
    new_k_coupon = k_prev - 1
    new_sum_coupon = dp[i - 1][k_prev]
    if new_sum_coupon < dp[i][new_k_coupon]:
        dp[i][new_k_coupon] = new_sum_coupon
        prev[i][new_k_coupon] = (k_prev, True)


def fill_dp_table(n, prices, dp, prev, max_k):
    """
    Заполняет таблицу dp и prev в соответствии с правилами
    начисления и использования купонов.
    """
    for i in range(1, n + 1):
        price = prices[i - 1]
        for k_prev in range(max_k + 1):
            process_purchase(i, k_prev, price, dp, prev, max_k)
            process_coupon_usage(i, k_prev, dp, prev)


def find_optimal_solution(n, dp, max_k):
    """
    Находит оптимальное решение (минимальную сумму и соответствующее
    количество купонов после покупки n товаров).
    """
    INF = float('inf')
    min_sum = INF
    best_k = 0

    for k in range(max_k + 1):
        if dp[n][k] < min_sum:
            min_sum = dp[n][k]
            best_k = k
        elif dp[n][k] == min_sum and k > best_k:
            best_k = k

    return min_sum, best_k


def reconstruct_solution(n, best_k, prev):
    """
    По таблице prev восстанавливает, на каких днях (покупках)
    купон использовался.
    """
    used_days = []
    current_k = best_k
    for i in range(n, 0, -1):
        if prev[i][current_k] is None:
            break
        k_prev, is_used = prev[i][current_k]
        if is_used:
            used_days.append(i)
        current_k = k_prev

    used_days.sort()
    return used_days


def compute_dp(n, prices):
    """
    Основная функция, которая инициализирует таблицы,
    заполняет их, находит оптимальное решение и восстанавливает
    список дней, когда использовались купоны.
    """
    max_k = n
    dp, prev = initialize_dp_tables(n, max_k)
    fill_dp_table(n, prices, dp, prev, max_k)
    min_sum, best_k = find_optimal_solution(n, dp, max_k)
    used_days = reconstruct_solution(n, best_k, prev)
    return min_sum, best_k, used_days



if __name__=="__main__":
    FILE_INPUT = "./txtf/input.txt"
    FILE_OUTPUT = "./txtf/output.txt"
    input_values = open_file_t18(FILE_INPUT)
    num, price = input_values[0], input_values[1]
    check = check_input_values_t18(num, price)
    if check:
        result = compute_dp(num, price)
        output_answer(result[0],result[1], result[2], FILE_OUTPUT)
    else:
        raise ValueError("ОШИБКА ВХОДНЫХ ДАННЫХ")
