import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from jumpgameII import jump

class TestJumpGameII(unittest.TestCase):
    def test_jump(self):
        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums2 = [2, 3, 0, 1, 4]

        self.assertEqual(jump(nums2),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

        nums1 = [2, 3, 1, 1, 4]

        self.assertEqual(jump(nums1),2)

if __name__ == '__main__':
       unittest.main()