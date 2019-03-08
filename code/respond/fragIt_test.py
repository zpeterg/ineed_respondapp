import unittest
from .fragIt import fragIt

sent = "The Raven. It's by Edgar Allan Poe. Once upon a midnight dreary, while..."
res = ('The', 'Raven', '.', 'It', "'s", 'by', 'Edgar', 'Allan', 'Poe', '.', 'Once', 'upon', 'a', 'midnight', 'dreary', ',', 'while', '...')

class TestFragment(unittest.TestCase):

    def test_break_to_token_words(self):
        self.assertEqual(fragIt(sent), res)

