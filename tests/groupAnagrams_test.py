import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.groupAnagrams import groupAnagrams

class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams_basic(self):
        input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

        self.assertEqual(sorted([sorted(group) for group in groupAnagrams(input1)]),
                         sorted([sorted(group) for group in expected_output1]))
        
if __name__ == '__main__':
       unittest.main()