import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.nthNode import ListNode, removeNthFromEnd

class TestRemoveNthnFromEnd(unittest.TestCase):
    def test_example_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = removeNthFromEnd(head, 2)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        
        self.assertEqual(result.next.next.val, 3)
        
        self.assertEqual(result.next.next.next.val, 5)

    def test_example_2(self):
        head = ListNode(1)
        result = removeNthFromEnd(head, 1)
        self.assertIsNone(result)
    
    def test_example_3(self):
        head = ListNode(1, ListNode(2))
        result = removeNthFromEnd(head, 1)

        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)

if __name__ == '__main__':
    unittest.main()