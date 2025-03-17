import unittest
import time
from memory_profiler import memory_usage
from lab_2.task_10.main import bst


class TestIsBST(unittest.TestCase):
    def test_empty_tree(self):
        """
        Пустое дерево (N=0) всегда является BST.
        """
        N = 0
        nodes = {}
        self.assertTrue(bst(N, nodes))

    def test_single_node(self):
        """
        Одноузловое дерево тоже всегда является BST.
        """
        N = 1
        # Только корень: ключ=5, нет детей
        nodes = {
            1: (5, 0, 0)
        }
        self.assertTrue(bst(N, nodes))

    def test_valid_bst(self):
        """
        Корректное дерево BST:
        """
        N = 3
        nodes = {
            1: (2, 2, 3),  # Первый узел: ключ=2, левый=2, правый=3
            2: (1, 0, 0),  # Второй узел: ключ=1, дети отсутствуют
            3: (3, 0, 0)   # Третий узел: ключ=3, дети отсутствуют
        }
        self.assertTrue(bst(N, nodes))

    def test_not_bst(self):
        """
        Некорректное дерево:
        """
        N = 3
        nodes = {
            1: (2, 2, 3),  # Корень: ключ=2, левый=2, правый=3
            2: (3, 0, 0),  # Левый узел: ключ=3 (больше родителя)
            3: (1, 0, 0)   # Правый узел: ключ=1 (меньше родителя)
        }
        self.assertFalse(bst(N, nodes))

    def test_time_and_memory(self):
        """
        Тест, который проверяет, что функция is_bst укладывается
        в ограничения по времени (2 секунды) и памяти (256 Мб).
        """
        start_time = time.time()
        start_mem = memory_usage()[0]

        # Пример данных для тестирования
        # (можно заменить на более крупный тест для проверки больших данных)
        N = 3
        nodes = {
            1: (2, 2, 3),
            2: (1, 0, 0),
            3: (3, 0, 0)
        }
        result = bst(N, nodes)

        end_time = time.time()
        end_mem = memory_usage()[0]

        elapsed_time = end_time - start_time
        used_mem = end_mem - start_mem

        # Проверяем корректность результата (для контроля)
        self.assertTrue(result, "Функция is_bst вернула False на валидных данных.")

        # Проверяем временной лимит (≤ 2 секунд)
        self.assertLessEqual(elapsed_time, 2.0,
                             f"Превышен лимит времени: {elapsed_time:.3f} c.")

        # Проверяем лимит памяти (≤ 256 Мб)
        # При этом memory_usage возвращает значение в MiB (мебибайтах),
        # соответственно сравниваем напрямую с 256
        self.assertLessEqual(used_mem, 256,
                             f"Превышен лимит памяти: {used_mem:.3f} MiB.")


if __name__ == '__main__':
    unittest.main()