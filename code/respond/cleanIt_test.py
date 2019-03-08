import unittest
from .cleanIt import cleanIt

class TestCleanIt(unittest.TestCase):

    def test_clean(self):
        arr = ('The', 'fish', "don't", 'taste', 'like', 'a', 'dozen', 'cats')
        resArr = ('fish', 'taste', 'like', 'dozen', 'cat')
        self.assertEqual(resArr, cleanIt(arr))

