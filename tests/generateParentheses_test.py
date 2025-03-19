import unittest

def generate_parentheses(n):

    def backtrack(s, left, right):

        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left +1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

    result = []
    backtrack("", 0, 0)
    return result

class TestGenerateParentheses(unittest.TestCase):
    def test_n_1(self):
        expected = ["()"]

        self.assertEqual(generate_parentheses(1), expected)

    def test_n_2(self):
        expected = ["(())", "()()"]

        self.assertEqual(generate_parentheses(2), expected)

if __name__ == "__main__":
    unittest.main()