import unittest
import time
import tracemalloc
from lab_1.task_18.main import compute_dp


class TestComputeDP(unittest.TestCase):
    def test_single_small_purchase(self):
        """
        Тест для одного платежа с ценой <= 100.
        Ожидаемый результат: стоимость оплаты равна сумме, купоны не выдаются.
        """
        n = 1
        prices = [50]
        expected = (50, 0, [])
        result = compute_dp(n, prices)
        self.assertEqual(result, expected)

    def test_single_purchase_with_coupon(self):
        """
        Тест для одного платежа с ценой > 100.
        Ожидаемый результат: стоимость оплаты равна сумме,
        выдаётся купон, поэтому k1 равен 1.
        """
        n = 1
        prices = [101]
        expected = (101, 1, [])
        result = compute_dp(n, prices)
        self.assertEqual(result, expected)

    def test_two_purchases(self):
        """
        Тест для двух покупок, когда использование купона выгодно.
        При ценах [101, 50] оптимально: оплачивается первый товар, а во втором используется купон.
        Ожидаемый результат: суммарная стоимость 101, оставшиеся купоны 0, купон использован во 2-ой покупке.
        """
        n = 2
        prices = [101, 50]
        expected = (101, 0, [2])
        result = compute_dp(n, prices)
        self.assertEqual(result, expected)

    def test_three_purchases(self):
        """
        Тест для трёх покупок с перемежающимся использованием купонов.
        При ценах [101, 101, 50] оптимальное решение приводит к суммарной стоимости 151,
        оставшихся купонов 0, купон использован во второй покупке.
        """
        n = 3
        prices = [101, 101, 50]
        expected = (151, 0, [2])
        result = compute_dp(n, prices)
        self.assertEqual(result, expected)

    def test_performance(self):
        """
        Тест для замера времени выполнения и использования памяти.
        Используется вход с 1000 покупками, где примерно половина цен > 100.
        """
        n = 1000
        prices = [150 if i % 2 == 0 else 50 for i in range(n)]

        start_time = time.perf_counter()
        tracemalloc.start()
        result = compute_dp(n, prices)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed_time = time.perf_counter() - start_time

        # Вывод затрат времени и памяти.
        print("Вывод затрат времени и памяти")
        print("Затраченное время: {:.6f} секунд(ы)".format(elapsed_time))
        print("Затраты памяти: {} Мбайт".format(peak/1024/1024))

        # Проверяем, что функция вернула корректный результат.
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()