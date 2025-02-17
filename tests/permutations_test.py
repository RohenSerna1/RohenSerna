import unittest
from itertools import permutations

class TestPermute(unittest.TestCase):
    def test_permute(self):
        # Caso 1
        nums1 = [1,2,3]
        expected1 = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

        self.assertEqual(sorted(permutations.permute(nums1)), sorted(expected1))

        # Caso 2
        nums2 = [0,1]
        expected2 = [[0,1], [1,0]]

        self.assertEqual(sorted(permutations.permute(nums2)), sorted(expected2))

        # Caso 3
        nums3 = [1]
        expected3 = [[1]]

        self.assertEqual(sorted(permutations.permute(nums3)), sorted(expected3))

        # Caso 4
        nums4 = []
        expected4 = []

        self.assertEqual(permutations.permute(nums4), permutations.permute(expected4))

        # Caso 5
        nums5 = [1,1]
        expected5 = [[1,1], [1,1]]

        self.assertEqual(sorted(permutations.permute(nums5)), sorted(expected5))

if __name__ == "__main__":
    unittest.main()