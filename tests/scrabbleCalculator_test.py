import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.scrabbleCalculator import calculate_scrabble_score

class TestScrabbleCalculator(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(calculate_scrabble_score("HEELLO"), 9)

    def test_case_2(self):
        self.assertEqual(calculate_scrabble_score("BYE"), 8)

if __name__ == '__main__':
    unittest.main()