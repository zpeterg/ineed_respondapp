import unittest
from .similarity import similarity


class TestSimilarity(unittest.TestCase):
    def test_similar(self):
        arr = ['dozen', 'cat']
        synoArr = [
            {'cat', 'lion', 'tiger'},
            {'12', 'dozen'},
            {'anchovies', 'fish'},
        ]
        res = {'count': 2, 'matching': ('cat', 'dozen'), 'syn_count': 2}
        self.assertEqual(res, similarity(arr, synoArr))
