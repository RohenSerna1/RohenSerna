import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.compareTriplets import compare_triplets

class TestCompareTriplets(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(compare_triplets([1, 2, 3], [3, 2, 1]), [1, 1])

    def test_case_2(self):
        self.assertEqual(compare_triplets([5, 6, 7], [3, 6, 10]), [1, 1])

if __name__ == '__main__':
    unittest.main()