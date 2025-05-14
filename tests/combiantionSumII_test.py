import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.combiantionSumII import combinationSum2

class TestCombinationSum2(unittest.TestCase):
    def test_example_1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertCountEqual(combinationSum2(candidates, target), expected)

    def test_example_2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        self.assertCountEqual(combinationSum2(candidates, target), expected)

if __name__ == "__main__":
    unittest.main()