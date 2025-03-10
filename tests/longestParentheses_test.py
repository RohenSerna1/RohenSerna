import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.longestParentheses import longest_valid_parentheses

class TestLongestValidParentheses(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(longest_valid_parentheses("(()"), 1)

    def test_simple_case(self):
        self.assertEqual(longest_valid_parentheses("(()()"), 2)

if __name__ == '__main__':
       unittest.main()