import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.balancedParenthesis import is_balanced

class TestBalancedParentheses(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(is_balanced("()"), "valid")

    def test_invalid_case(self):
        self.assertEqual(is_balanced(")("), "invalid")

if __name__ == '__main__':
    unittest.main()