import unittest
import psutil
import time
from lab_1.task_16.main import min_path


class TestMinPath(unittest.TestCase):
    def test_min_path_simple(self):
        """
        Тест на простом примере из двух городов.
        """
        num = 2
        matrix = [
            [0, 10],
            [10, 0]
        ]
        dist, path = min_path(num, matrix)
        self.assertEqual(dist, "10")  # Единственный путь: 1 -> 2
        self.assertEqual(path, [2, 1])  # Путь возвращается в обратном порядке

    def test_min_path_three_nodes(self):
        """
        Тест на примере из трех городов.
        """
        num = 3
        matrix = [
            [0, 1, 5],
            [1, 0, 2],
            [5, 2, 0]
        ]
        dist, path = min_path(num, matrix)
        # Возможные пути (из города 1):
        #   1->2->3: 1 + 2 = 3
        #   1->3->2: 5 + 2 = 7
        # Минимальный = 3, значит путь 1->2->3
        # Возвращается в обратном порядке [3, 2, 1]
        self.assertEqual(dist, "3")
        self.assertEqual(path, [3, 2, 1])

    def test_min_path_identical_weights(self):
        """
        Тестирование функции, когда между любыми двумя городами равные расстояния.
        """
        num = 4
        matrix = [
            [0, 2, 2, 2],
            [2, 0, 2, 2],
            [2, 2, 0, 2],
            [2, 2, 2, 0]
        ]
        dist, path = min_path(num, matrix)
        # При равных расстояниях все пути дают одинаковую сумму:
        #   Для 4 городов любой цикл (исключая стартовый переход) даст:
        #     sum = 2*(количество переходов) = 2*(num-1) = 6
        # Возвращённый путь зависит от первой найденной перестановки
        self.assertEqual(dist, "6", "Минимальное расстояние должно быть 6.")

    def test_min_path_time_and_memory(self):
        """
        Тест для проверки времени и памяти с использованием psutil.
        """
        num = 6
        # Генерируем псевдослучайную матрицу, но здесь она фиксирована для воспроизводимости.
        # При желании можно рандомизировать.
        matrix = [
            [0, 2, 9, 10, 7, 3],
            [2, 0, 1, 4, 11, 8],
            [9, 1, 0, 14, 2, 6],
            [10, 4, 14, 0, 15, 5],
            [7, 11, 2, 15, 0, 1],
            [3, 8, 6, 5, 1, 0]
        ]

        process = psutil.Process()
        mem_before = process.memory_info().rss
        start_time = time.time()

        dist, path = min_path(num, matrix)

        end_time = time.time()
        mem_after = process.memory_info().rss
        elapsed_time = end_time - start_time
        used_memory = (mem_after - mem_before) / 1024.0 / 1024.0

        print(f"Время выполнения: {elapsed_time:.5f} сек.")
        print(f"Дополнительная использованная память: {used_memory:.5f} МБ.")
        print(f"Результат: {dist}, путь: {path}")

        # Проверяем, что алгоритм достаточно быстрый для num=6.
        self.assertTrue(elapsed_time < 2, "Время выполнения превысило 2 секунды.")
        # Проверяем, что алгоритм не расходует слишком много памяти (условная проверка для примера).
        self.assertTrue(used_memory < 50, "Превышен лимит памяти в 50 МБ.")


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)