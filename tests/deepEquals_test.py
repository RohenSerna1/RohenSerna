import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.deepEquals import deep_equals

class TestDeepEquals(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(deep_equals({'a': 1, 'b': {'c': 3}}, {'a': 1, 'b': {'c': 3}}))

    def test_case_2(self):
        self.assertFalse(deep_equals({'a': 1, 'b': {'c': 5}}, {'a': 1, 'b': {'c': 6}}))

if __name__ == '__main__':
    unittest.main()