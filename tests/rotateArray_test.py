import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.rotateArray import rotate

class TestRotateArray(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_case_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        rotate(nums, k)
        self.assertEqual(nums, [3, 99, -1, -100])

if __name__ == '__main__':
    unittest.main()