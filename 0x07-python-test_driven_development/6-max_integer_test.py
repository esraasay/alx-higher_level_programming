#!/usr/bin/python3
import unittest
from your_module_name import max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    
    def test_basic_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 0, 10, -3]), 10)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 1.2]), 2.7)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(["apple", "orange", "banana"])

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 10000000]), 10000000)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])

    def test_mixed_data_types_float(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3.5])

if __name__ == '__main__':
    unittest.main()
