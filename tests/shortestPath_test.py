import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.shortestPath import shortest_path

class TestShortestPath(unittest.TestCase):
    def test_case_1(self):
        graph = [
            [0, 2, 6, 0, 0, 0, 0],
            [2, 0, 0, 5, 0, 0, 0],
            [6, 0, 0, 8, 0, 0, 0],
            [0, 5, 8, 0, 10, 15, 0],
            [0, 0, 0, 10, 0, 6, 2],
            [0, 0, 0, 15, 6, 0, 6],
            [0, 0, 0, 0, 2, 6, 0]
        ]
        start_node = 0
        end_node = 6
        expected_path = [0, 1, 3, 4, 6]
        path = shortest_path(graph, start_node, end_node)
        self.assertEqual(path, expected_path)

    def test_case_no_path(self):
        graph = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        start_node = 0
        end_node = 2
        expected_path = []
        path = shortest_path(graph, start_node, end_node)
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()