import unittest
import random
import time
import psutil
from lab_1.task_8.main import sort_lectures, max_lectures

class TestLectures(unittest.TestCase):
    def test_sort_lectures_empty(self):
        lectures = []
        sorted_lectures = sort_lectures(lectures)
        self.assertEqual(sorted_lectures, [])

    def test_sort_lectures_single(self):
        lectures = [(1, 2)]
        sorted_lectures = sort_lectures(lectures)
        self.assertEqual(sorted_lectures, [(1, 2)])

    def test_sort_lectures_multiple(self):
        lectures = [(2, 3), (1, 4), (3, 5), (0, 2)]
        # Ожидаем, что сортировка будет по второму элементу (время окончания)
        expected = [(0, 2), (2, 3), (1, 4), (3, 5)]
        sorted_lectures = sort_lectures(lectures)
        self.assertEqual(sorted_lectures, expected)

    def test_max_lectures_zero_asks(self):
        asks = 0
        lectures = [(1, 2), (2, 3)]
        self.assertEqual(max_lectures(asks, lectures), 0)

    def test_max_lectures_one_ask(self):
        asks = 1
        lectures = [(1, 2), (2, 3)]
        # Если нужно провести всего 1 лекцию, то результат = 1
        self.assertEqual(max_lectures(asks, lectures), 1)

class TestMemoryTime(unittest.TestCase):
    def test_large_random_input(self):
        """
        Данный тест генерирует случайный набор лекций и замеряет время запуска функций.
        При необходимости можно добавить контроль использования памяти.
        """
        # Генерация большого числа случайных интервалов
        n = 10000  # Можно менять величину для более серьёзной нагрузки
        lectures = []
        for _ in range(n):
            start = random.randint(0, 10**6)
            end = start + random.randint(1, 1000)  # Гарантируем, что конец ≥ старта
            lectures.append((start, end))

        asks = random.randint(1, n)  # Случайное значение asks

        # Замер времени
        start_time = time.time()
        result = max_lectures(asks, lectures)
        end_time = time.time()
        process = psutil.Process()
        memory_usage = process.memory_info().rss

        elapsed_time = end_time - start_time

        print(f"Затраченное время: {elapsed_time} секунд(ы).")
        print(f"Используемая память: {memory_usage/1024/1024} Мбайт.")

        self.assertTrue(elapsed_time < 2, "Время выполнения превысило 2 секунды в тестах.")

if __name__ == '__main__':
    unittest.main()