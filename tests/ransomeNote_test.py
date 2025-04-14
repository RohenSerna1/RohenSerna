import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ransomeNote import ransomNote

class TestRansomNote(unittest.TestCase):
    def test_example_true(self):
        self.assertTrue(ransomNote("abc", "cbad"))
    
    def test_example_true(self):
        self.assertFalse(ransomNote("aa", "ab"))
    
if __name__ == '__main__':
       unittest.main()