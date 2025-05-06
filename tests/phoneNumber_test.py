import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.phoneNumber import letter_combinations

class TestLetterCombinations(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(letter_combinations("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])

    def test_case_2(self):
        self.assertEqual(letter_combinations("2"), ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()