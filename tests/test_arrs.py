import unittest
from utils.arrs import get, my_slice


class TestArrs(unittest.TestCase):
    def test_get_existing_index(self):
        """Тест для функции get() с существующим индексом"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(get(arr, 2), 3)

    def test_get_non_existing_index_with_default(self):
        """Тест для функции get() с несуществующим индексом и значением по умолчанию"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(get(arr, 10, default=-1), -1)

    def test_my_slice_start_and_end(self):
        """Тест для функции my_slice() с указанием начального и конечного индексов"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr, start=1, end=4), [2, 3, 4])

    def test_my_slice_start_only(self):
        """Тест для функции my_slice() только с указанием начального индекса"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr, start=2), [3, 4, 5])

    def test_my_slice_end_only(self):
        """Тест для функции my_slice() только с указанием конечного индекса"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr, end=3), [1, 2, 3])

    def test_my_slice_empty_list(self):
        """Тест для функции my_slice() с пустым списком"""
        arr = []
        self.assertEqual(my_slice(arr), [])

    def test_my_slice_negative_start_and_end(self):
        """Тест для функции my_slice() с отрицательными начальным и конечным индексами"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr, start=-3, end=-1), [3, 4])


if __name__ == '__main__':
    unittest.main()