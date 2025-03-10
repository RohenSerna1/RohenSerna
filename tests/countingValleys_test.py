import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.countingValleys import countingValleys

class TestCountingValleys(unittest.TestCase):
    def test_example_1(self):
        steps = 8
        path = "UDDDUDUU"

        self.assertEqual(countingValleys(steps, path), 1)

    def test_example_2(self):
        steps = 12
        path = "DDUUDDUDUUUD"

        self.assertEqual(countingValleys(steps, path), 2)

    def test_example_3(self):
            steps = 6
            path = "UUUDDD"

            self.assertEqual(countingValleys(steps, path), 0)

    def test_example_4(self):
            steps = 8
            path = "DDDUUUUU"

            self.assertEqual(countingValleys(steps, path), 1)

    def test_example_5(self):
            steps = 10
            path = "UDUDUDUDUD"

            self.assertEqual(countingValleys(steps, path), 0)

    def test_example_6(self):
            steps = 2
            path = "DU"

            self.assertEqual(countingValleys(steps, path), 1)

    def test_example_7(self):
            steps = 2
            path = "UD"

            self.assertEqual(countingValleys(steps, path), 0)

if __name__ == '__main__':
       unittest.main()