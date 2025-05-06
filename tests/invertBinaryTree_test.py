import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def levelOrder(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        current_level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result

class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_tree_example_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        inverted_root = invertTree(root)
        expected_output = [[4], [7, 2], [9, 6, 3, 1]]
        self.assertEqual(levelOrder(inverted_root), expected_output)

    def test_invert_tree_example_2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        inverted_root = invertTree(root)
        expected_output = [[2], [3, 1]]
        self.assertEqual(levelOrder(inverted_root), expected_output)

if __name__ == '__main__':
    unittest.main()