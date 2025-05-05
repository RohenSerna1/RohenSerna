import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.additiveNumber import is_additive_number

class TestAdditiveNumber(unittest.TestCase):
    def test_valid_additive_number(self):
        self.assertTrue(is_additive_number("112358"))

    def test_invalid_additive_number(self):
        self.assertFalse(is_additive_number("102"))

if __name__ == '__main__':
    unittest.main()