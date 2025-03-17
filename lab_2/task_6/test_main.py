import unittest
import time
import tracemalloc
from lab_2.task_6.main import is_binary_search_tree


class TestBinarySearchTree(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(is_binary_search_tree([]))

    def test_single_node(self):
        self.assertTrue(is_binary_search_tree([(10, -1, -1)]))

    def test_valid_bst_small(self):
        nodes = [
            (10, 1, 2),  # корень (индекс 0)
            (5, -1, -1),  # левый (индекс 1)
            (15, -1, -1)  # правый (индекс 2)
        ]
        self.assertTrue(is_binary_search_tree(nodes))

    def test_valid_bst_complex(self):
        nodes = [
            (10, 1, 2),  # корень (индекс 0)
            (5, 3, 4),  # левое поддерево (индекс 1)
            (15, 5, 6),  # правое поддерево (индекс 2)
            (3, -1, -1),  # лист (индекс 3)
            (7, -1, -1),  # лист (индекс 4)
            (12, -1, -1),  # лист (индекс 5)
            (20, -1, -1)  # лист (индекс 6)
        ]
        self.assertTrue(is_binary_search_tree(nodes))

    def test_invalid_bst_left(self):
        nodes = [
            (10, 1, 2),
            (12, -1, -1),  # левый (индекс 1) - должен быть < 10
            (15, -1, -1)
        ]
        self.assertFalse(is_binary_search_tree(nodes))

    def test_invalid_bst_right(self):
        nodes = [
            (10, 1, 2),
            (5, -1, -1),
            (8, -1, -1)  # правый (индекс 2) - должен быть > 10
        ]
        self.assertFalse(is_binary_search_tree(nodes))

    def test_invalid_bst_transitive(self):
        nodes = [
            (10, 1, 2),
            (5, 3, 4),
            (15, 5, 6),
            (3, -1, -1),
            (20, -1, -1),  # должен быть < 10
            (12, -1, -1),
            (17, -1, -1)
        ]
        self.assertFalse(is_binary_search_tree(nodes))

    def test_large_tree_performance(self):
        # Создаем большое дерево (10,000 узлов)
        n = 10000
        # Создаем корректное бинарное дерево поиска
        nodes = []
        for i in range(n):
            left = 2 * i + 1 if 2 * i + 1 < n else -1
            right = 2 * i + 2 if 2 * i + 2 < n else -1
            nodes.append((i, left, right))

        # Начинаем отслеживание памяти для этого конкретного теста
        tracemalloc.start()

        # Измеряем время выполнения
        start_time = time.time()
        result = is_binary_search_tree(nodes)
        end_time = time.time()
        execution_time = end_time - start_time

        # Измеряем использование памяти
        current, peak = tracemalloc.get_traced_memory()

        # Останавливаем отслеживание памяти
        tracemalloc.stop()

        # Выводим результаты измерений
        print(f"\nВремя выполнения для дерева из {n} узлов: {execution_time:.6f} сек")
        print(f"Затраты памяти: {peak / 1024 / 1024:.6f} МБ")

        self.assertFalse(result)
        self.assertLess(execution_time, 10.0)  # Проверяем, что выполняется меньше 10 секунд
        self.assertLess(peak / (1024 * 1024), 512.0)  # Проверяем, что использование памяти меньше 512 МБ


if __name__ == '__main__':
    # Запускаем отслеживание использования памяти
    tracemalloc.start()
    # Запускаем тесты
    unittest.main(exit=False)
    # Получаем текущее и пиковое использование памяти
    current, peak = tracemalloc.get_traced_memory()
    # Останавливаем отслеживание
    tracemalloc.stop()