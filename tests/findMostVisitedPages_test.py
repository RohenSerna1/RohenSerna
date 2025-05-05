import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.findMostVisitedPages import findMostVisitedPages

class TestFindMostVisitedPages(unittest.TestCase):
    
    def test_case_1(self):
        logData = [
            {"url": "/home", "userId": "A"},
            {"url": "/about", "userId": "B"},
            {"url": "/products", "userId": "A"},
            {"url": "/home", "userId": "C"},
            {"url": "/contact", "userId": "B"},
            {"url": "/products", "userId": "D"},
            {"url": "/home", "userId": "A"},
            {"url": "/home", "userId": "B"},
            {"url": "/products", "userId": "A"}
        ]
        expected = ['/home', '/products', '/about', '/contact']
        self.assertEqual(findMostVisitedPages(logData), expected)

    def test_case_2(self):
        logData = [
            {"url": "/x", "userId": "1"},
            {"url": "/y", "userId": "1"},
            {"url": "/z", "userId": "2"},
            {"url": "/x", "userId": "2"},
            {"url": "/y", "userId": "3"},
            {"url": "/z", "userId": "2"},
            {"url": "/x", "userId": "1"}
        ]
        expected = ['/x', '/y', '/z']
        self.assertEqual(findMostVisitedPages(logData), expected)

if __name__ == "__main__":
    unittest.main()