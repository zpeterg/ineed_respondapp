import unittest
from .synomize import spell_suggest, synomize


class TestSynomize(unittest.TestCase):
    def test_synomize(self):
        arr = ['fish', 'taste', 'like', 'dozen', 'cat']
        res = (
            ('African_tea', 'Arabian_tea', 'CAT', 'CT', 'Caterpillar', 'barf', 'be_sick', 'big_cat', 'bozo', 'cast', 'cat', "cat-o'-nine-tails", 'chuck', 'computed_axial_tomography', 'computed_tomography', 'computerized_axial_tomography', 'computerized_tomography', 'disgorge', 'guy', 'hombre', 'honk', 'kat', 'khat', 'puke', 'purge', 'qat', 'quat', 'regorge', 'regurgitate', 'retch', 'sick', 'spew', 'spue', 'throw_up', 'true_cat', 'upchuck', 'vomit', 'vomit_up'),
            ('12', 'XII', 'dozen', 'twelve', 'xii'),
            ('Fish', 'Pisces', 'Pisces_the_Fishes', 'angle', 'fish'),
            ('alike', 'care', 'comparable', 'corresponding', 'ilk', 'like', 'same', 'similar', 'the_like', 'the_likes_of', 'wish'),
            ('appreciation', 'discernment', 'gustation', 'gustatory_modality', 'gustatory_perception', 'gustatory_sensation', 'mouthful', 'penchant', 'perceptiveness', 'predilection', 'preference', 'sample', 'savor', 'savour', 'sense_of_taste', 'smack', 'taste', 'taste_perception', 'taste_sensation', 'tasting', 'try', 'try_out')
        )
        self.assertEqual(res, synomize(arr))

    def test_spell_suggest(self):
        words = ['something', 'is', 'hapenning', 'here']
        res = ('hapenning', 'happening', 'henning', 'here', 'is', 'penning', 'something')
        self.assertEqual(res, spell_suggest(words))

    def test_spelling_and_synomize(self):
        arr = ('fishys',)
        res = (
            ('Fish', 'Pisces', 'Pisces_the_Fishes', 'angle', 'fish', 'fishes'),
            ('fishy', 'funny', 'shady', 'suspect', 'suspicious'),
            ('fishys',),
        )
        self.assertEqual(res, synomize(arr))
