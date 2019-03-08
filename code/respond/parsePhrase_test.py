import unittest
from .synomize import synomize
from .flatten import prepPhrase
from .parsePhrase import parsePhrase

syn_phrase = synomize(prepPhrase('I would like to hear about help with house rent in the Siloam area'))
syn_phrase2 = synomize(prepPhrase('I would like to hear about help with house rent in the Siloam Springs area'))

class TestParsePhrase(unittest.TestCase):

    def test_parse_phrase(self):
        arr = ('housing assistance', 'Siloam Springs')
        res = {'count': 2, 'similarity': 2, 'lastCount': 1, 'lastSimilarity': 1, 'matching': ('assist', 'assistance', 'loam')}
        self.maxDiff = None
        self.assertEqual(res, parsePhrase(arr, syn_phrase))

    def test_parse_phrase_that_is_more_similar(self):
        arr = ('housing assistance', 'Siloam Springs')
        res = {'count': 2, 'similarity': 2, 'lastCount': 1, 'lastSimilarity': 1, 'matching': ('assist', 'assistance', 'loam')}
        self.maxDiff = None

        self.assertEqual(res, parsePhrase(arr, syn_phrase2))
