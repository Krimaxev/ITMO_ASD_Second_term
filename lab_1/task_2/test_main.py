import unittest
import time
import tracemalloc
from lab_1.task_2.main import min_refills


class TestMinRefills(unittest.TestCase):
    def test_no_refill_needed(self):
        d = 300
        m = 400
        stops = []
        n = len(stops)
        self.assertEqual(min_refills(d, m, n, stops), 0)

    def test_sample(self):
        d = 950
        m = 400
        stops = [200, 375, 550, 750]
        n = len(stops)
        self.assertEqual(min_refills(d, m, n, stops), 2)

    def test_impossible_to_reach(self):
        d = 950
        m = 400
        stops = [500, 600, 700, 800]
        n = len(stops)
        self.assertEqual(min_refills(d, m, n, stops), -1)

    def test_multiple_refills(self):
        d = 800
        m = 200
        stops = [150, 350, 550, 750]
        n = len(stops)
        self.assertEqual(min_refills(d, m, n, stops), 4)

    def test_single_stop_impossible(self):
        d = 500
        m = 100
        stops = [100]
        n = len(stops)
        self.assertEqual(min_refills(d, m, n, stops), -1)

    def test_performance_and_memory(self):
        d = 10 ** 6
        m = 5000
        stops = list(range(m, d, m))
        n = len(stops)

        tracemalloc.start()
        start_time = time.perf_counter()

        result = min_refills(d, m, n, stops)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time
        peak_mb = peak / (1024 * 1024)

        print(f"\nTest time and memory:")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Memory usage: {peak_mb:.4f} MB")

        self.assertLessEqual(execution_time, 2, f"Execution time {execution_time} exceeds threshold")
        self.assertLessEqual(peak_mb, 50, f"Peak memory usage {peak_mb} MB exceeds threshold")
        self.assertEqual(result, len(stops))


if __name__ == '__main__':
    unittest.main(verbosity=2)