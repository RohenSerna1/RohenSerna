import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.armstrongNumbers import is_armstrong

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertTrue(is_armstrong(153))

    def test_not_armstrong_number(self):
        self.assertFalse(is_armstrong(123))

if __name__ == '__main__':
       unittest.main()