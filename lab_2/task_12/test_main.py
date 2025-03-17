import unittest
import time
import tracemalloc
from lab_2.task_12.main import balance_binary_tree


class TestBalanceBinaryTree(unittest.TestCase):
    def test_empty_tree(self):
        # Тестируем случай пустого дерева.
        data = [0]
        expected = []
        result = balance_binary_tree(data)
        self.assertEqual(result, expected)

    def test_single_node(self):
        # Тестируем дерево, состоящее из одного узла.
        data = [1, 42, 0, 0]  # ключ 42, оба ребёнка отсутствуют.
        expected = [0]
        result = balance_binary_tree(data)
        self.assertEqual(result, expected)

    def test_left_skewed_tree(self):
        # Тестируем дерево, где каждый узел имеет только левого ребенка
        n = 5
        data = [n]
        for i in range(1, n + 1):
            key = i
            left = i + 1 if i < n else 0
            right = 0
            data.extend([key, left, right])
        result = balance_binary_tree(data)

        expected = []
        heights = {}
        for i in range(n, 0, -1):
            h = 0 if i == n else heights[i + 1] + 1
            heights[i] = h
        for i in range(1, n + 1):
            left_h = heights[i + 1] if i < n else -1
            right_h = -1
            expected.append(right_h - left_h)
        self.assertEqual(result, expected)

    def test_right_skewed_tree(self):
        # Тестируем дерево, где каждый узел имеет только правого ребенка (цепочка).
        n = 5
        data = [n]
        for i in range(1, n + 1):
            key = i
            left = 0  # левого ребенка нет
            right = i + 1 if i < n else 0  # правый ребёнок до последнего узла
            data.extend([key, left, right])
        result = balance_binary_tree(data)
        # Аналогично вычисляем ожидаемые значения:
        expected = []
        heights = {}
        for i in range(n, 0, -1):
            h = 0 if i == n else heights[i + 1] + 1
            heights[i] = h
        for i in range(1, n + 1):
            left_h = -1
            right_h = heights[i + 1] if i < n else -1
            expected.append(right_h - left_h)
        self.assertEqual(result, expected)

    def test_balanced_tree(self):
        # Тестируем сбалансированное дерево.
        data = [
            3,
            10, 2, 3,
            20, 0, 0,
            30, 0, 0
        ]
        expected = [0, 0, 0]
        result = balance_binary_tree(data)
        self.assertEqual(result, expected)

    def test_large_tree_performance(self):
        # Тест производительности: генерируем большое дерево (цепочка) из 100000 узлов.
        n = 100000
        data = [n]
        for i in range(1, n + 1):
            key = i
            left = i + 1 if i < n else 0
            right = 0
            data.extend([key, left, right])

        start_time = time.time()
        _ = balance_binary_tree(data)
        elapsed = time.time() - start_time
        self.assertTrue(elapsed < 2, f"Функция работает слишком медленно: {elapsed:.4f} секунд")

    def test_memory_usage(self):
        # Тест использования памяти для большого дерева.
        n = 100000
        data = [n]
        for i in range(1, n + 1):
            key = i
            left = i + 1 if i < n else 0
            right = 0
            data.extend([key, left, right])

        tracemalloc.start()
        _ = balance_binary_tree(data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        self.assertTrue(peak < 256 * 1024 * 1024,
                        f"Пиковое использование памяти слишком велико: {peak / (1024 * 1024):.2f} МБ")


if __name__ == '__main__':
    unittest.main()