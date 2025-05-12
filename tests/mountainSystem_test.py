import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.mountainSystem import simulate_landslides

class TestSimulateLandslides(unittest.TestCase):
    def test_case_1(self):
        mountain_system = [
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', 'X', '-', 'X', '-', '-', '-'],
            ['X', '-', 'X', '-', '-', 'X', '-'],
            ['-', 'X', '-', 'X', '-', 'X', 'X'],
            ['X', 'X', '-', 'X', '-', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        thousand_years = 6
        expected_output = [
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', '-', 'X', '-', '-', '-'],
            ['X', 'X', 'X', '-', '-', 'X', '-'],
            ['-', 'X', 'X', 'X', '-', 'X', 'X'],
            ['X', 'X', 'X', 'X', '-', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        result = simulate_landslides(mountain_system, thousand_years)
        self.assertEqual(result, expected_output)

    def test_case_no_change(self):
        mountain_system = [
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', '-', '-', '-', 'X', '-'],
            ['-', '-', '-', '-', '-', 'X', '-']
        ]
        thousand_years = 5
        expected_output = mountain_system
        result = simulate_landslides(mountain_system, thousand_years)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()