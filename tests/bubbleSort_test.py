import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.bubbleSort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_unsorted_list(self):
        lista = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(lista)
        self.assertEqual(lista, [11, 12, 22, 25, 34, 64, 90])

    def test_sorted_list(self):
        lista = [1, 2, 3, 4, 5]
        bubble_sort(lista)
        self.assertEqual(lista, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()