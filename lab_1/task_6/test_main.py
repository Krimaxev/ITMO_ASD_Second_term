import unittest
import time
import tracemalloc
from lab_1.task_6.main import largest_number

class TestLargestNumber(unittest.TestCase):
    def test_basic(self):
        # Проверяем базовый случай.
        self.assertEqual(largest_number([23, 39, 92]), "923923")

    def test_single_element(self):
        # Если список состоит из одного элемента, то функция должна вернуть его строковое представление.
        self.assertEqual(largest_number([5]), "5")

    def test_same_numbers(self):
        # Если все числа одинаковы, то они должны просто соединиться.
        self.assertEqual(largest_number([10, 10, 10]), "101010")

    def test_already_sorted(self):
        # Тест, когда список уже отсортирован в нужном порядке.
        self.assertEqual(largest_number([9, 5, 34, 3, 30]), "9534330")

    def test_performance_and_memory(self):
        import random
        random.seed(42)
        large_input = [random.randint(1, 100) for _ in range(1000)]

        tracemalloc.start()
        start_time = time.perf_counter()
        result = largest_number(large_input)
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time
        peak_memory_mb = peak / (1024 * 1024)

        # Вывод расчётов затрат времени и памяти.
        print("\nРасчет затрат времени и памяти")
        print(f"Затраты времени: {execution_time:.4f} секунд(ы)")
        print(f"Затраты памяти: {peak_memory_mb:.4f} MB")

        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()