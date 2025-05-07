import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.coin import min_coins

class TestCoinChange(unittest.TestCase):
    def test_case_1(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(min_coins(coins, amount), 3)

    def test_case_2(self):
        coins = [2]
        amount = 3
        self.assertEqual(min_coins(coins, amount), -1)

    def test_case_3(self):
        coins = [1]
        amount = 0
        self.assertEqual(min_coins(coins, amount), 0)

    def test_case_4(self):
        coins = [1, 3, 4]
        amount = 6
        self.assertEqual(min_coins(coins, amount), 2)  # 3 + 3 or 4 + 1

    def test_case_5(self):
        coins = [5, 10]
        amount = 7
        self.assertEqual(min_coins(coins, amount), -1)

if __name__ == '__main__':
    unittest.main()