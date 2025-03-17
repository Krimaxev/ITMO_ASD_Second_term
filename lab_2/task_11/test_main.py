import unittest
import time
import tracemalloc
import random
from lab_2.task_11.main import balanced_binary_tree


class TestBalancedBinaryTree(unittest.TestCase):
    def test_insert_exists_delete(self):
        # Тест базовых операций: insert, exists, delete
        ops = ["insert", "5", "exists", "5", "delete", "5", "exists", "5"]
        expected = "true\nfalse\n"
        result = balanced_binary_tree(ops)
        self.assertEqual(result, expected)

    def test_next_operation(self):
        # Тест операции next: должен вернуть минимальное число > заданного
        ops = ["insert", "2", "insert", "3", "insert", "6", "next", "3"]
        expected = "6\n"
        result = balanced_binary_tree(ops)
        self.assertEqual(result, expected)

    def test_prev_operation(self):
        # Тест операции prev: должен вернуть максимальное число < заданного
        ops = ["insert", "2", "insert", "3", "insert", "6", "prev", "6"]
        expected = "3\n"
        result = balanced_binary_tree(ops)
        self.assertEqual(result, expected)

    def test_combined_operations(self):
        # Комбинированный тест операций
        ops = [
            "insert", "5",
            "insert", "3",
            "insert", "7",
            "exists", "3",
            "delete", "3",
            "exists", "3",
            "next", "5",
            "prev", "7"
        ]
        # Ожидается: exists 3 -> true, exists 3 -> false, next 5 -> 7, prev 7 -> 5
        expected = "true\nfalse\n7\n5\n"
        result = balanced_binary_tree(ops)
        self.assertEqual(result, expected)

    def test_performance_and_memory(self):
        # Тест производительности и использования памяти.
        # Генерируем большое количество операций для имитации нагруженного сценария.
        ops = []
        count = 100000
        # Заполняем множество операциями insert случайными числами от 0 до 9
        numbers = [str(random.randint(0, 9)) for _ in range(count)]
        for num in numbers:
            ops.extend(["insert", num])
        # Добавляем 1000 случайных запросов (exists, next, prev)
        for _ in range(1000):
            x = str(random.randint(0, 9))
            op = random.choice(["exists", "next", "prev"])
            ops.extend([op, x])

        # Начинаем трассировку памяти
        tracemalloc.start()
        start_time = time.time()

        # Выполнение функции
        _ = balanced_binary_tree(ops)

        elapsed_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Проверяем, что время выполнения не превышает 2 секунд.
        self.assertLessEqual(elapsed_time, 2, f"Время выполнения {elapsed_time} сек, превышает лимит 2 сек.")
        # Проверяем, что пиковое использование памяти не превышает 512 Мб.
        self.assertLessEqual(peak, 512 * 1024 * 1024,
                             f"Пиковое использование памяти {peak} байт, превышает лимит 512 Мб.")


if __name__ == "__main__":
    unittest.main()