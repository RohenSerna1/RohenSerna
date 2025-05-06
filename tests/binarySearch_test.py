import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.binarySearch import binary_search

class TestBinarySearchCounter(unittest.TestCase):
    def test_case_found(self):
        number_list = [10, 11, 12, 16, 18, 23, 29, 33, 48, 54, 57, 68, 77, 84, 98]
        result = binary_search(number_list, 48)
        self.assertIn("Number found in index:", result)
        self.assertIn("Total Number of keys examined:", result)

    def test_case_not_found(self):
        number_list = [10, 11, 12, 16, 18, 23, 29, 33, 48, 54, 57, 68, 77, 84, 98]
        result = binary_search(number_list, 100)
        self.assertIn("Number not found", result)
        self.assertIn("Total Number of keys examined:", result)

if __name__ == '__main__':
    unittest.main()