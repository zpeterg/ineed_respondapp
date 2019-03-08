import unittest
from .flatten import flatten, clean_child, prepPhrase

resources = [
    {
        "name": "fishes",
        "keywords": ("fish seafood animal",),
        "phrase": ("It looks like you're looking for fishes.",),
        "options": ("What kind of fishes are you looking for?",),
        "children": (
            {
                "name": "deep sea fishes",
                "keywords": ("deep bottom-dwellers",),
                "phrase": ("We have several fishes that swim deep.",),
                "children": [
                    {
                        "name": "Angler Fish",
                        "keywords": ("Angler Lophiiformes",),
                        "info": ({"name": "It has a light"},),
                        "isLeaf": True,
                        "phrase": ("Angler Fish",),
                    },
                    {
                        "name": "Sword Fish",
                        "keywords": ("Sword Xiphias",),
                        "info": ({"name": "Unusual characteristics", "value": "sword"},),
                        "isLeaf": True,
                        "phrase": ("Sword Fish",),
                    }
                ]
            },
        )
    },
    {
        "name": "eels",
        "keywords": ("eel snake-like",),
        "phrase": ("Are you looking for eels?",),
        "options": ("What kind of eels are you looking for?",),
        "children": (
            {
                "name": "Synder's Moray",
                "keywords": ("Synder's finespot Moray",),
                "info": ({"name": "It was discovered in 1904"},),
                "isLeaf": True,
                "phrase": ("Snyder's Moray",),
            },
            {
                "name": "Zebra Moray",
                "keywords": ("Zebra striped Moray",),
                "info": ({"name": "Diet", "value": "Sea urchins, mollusks, and crustaceans."},),
                "isLeaf": True,
                "phrase": ("Zebra Moray",),
            },
        )
    }
]

phrase = 'I would like to hear about help with house rent in the Siloam area'

class TestFlatten(unittest.TestCase):
    def test_prep_phrase(self):
        res = ('would', 'like', 'hear', 'help', 'house', 'rent', 'siloam', 'area')
        self.assertEqual(res, prepPhrase(phrase))

    def test_clean_child(self):
        parent_keywords = (('fish',), ('cow',))
        keywords = ('panther', 'cow', 'antelope')
        res = ('panther', 'antelope')
        self.assertEqual(clean_child(parent_keywords, keywords), res)

    def test_flatten(self):

        res = [
            {
                'subject': ('fishes',),
                'keywords': (('fish', 'seafood', 'animal'),),
                'phrase': ("It looks like you're looking for fishes.",),
                'options': ('What kind of fishes are you looking for?',),
                'children': ('We have several fishes that swim deep.',)
            },
            {
                'subject': ('fishes', 'deep sea fishes'),
                'keywords': (('fish', 'seafood', 'animal'), ('deep', 'bottom-dweller')),
                'phrase': ('We have several fishes that swim deep.',),
                'children': ('Angler Fish', 'Sword Fish')
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Angler Fish'),
                'keywords': (('fish', 'seafood', 'animal'), ('deep', 'bottom-dweller'), ('angler', 'lophiiformes')),
                'phrase': ('Angler Fish',),
                'info': ({'name': 'It has a light'},),
                'isLeaf': True
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Sword Fish'),
                'keywords': (('fish', 'seafood', 'animal'), ('deep', 'bottom-dweller'), ('sword', 'xiphias')),
                'phrase': ('Sword Fish',),
                'info': ({'name': 'Unusual characteristics', 'value': 'sword'},),
                'isLeaf': True
            },
            {
                'subject': ('eels',),
                'keywords': (('eel', 'snake-like'),),
                'phrase': ('Are you looking for eels?',),
                'options': ('What kind of eels are you looking for?',),
                'children': ("Snyder's Moray", 'Zebra Moray')
            },
            {
                'subject': ('eels', "Synder's Moray"),
                'keywords': (('eel', 'snake-like'), ('synder', "'s", 'finespot', 'moray')),
                'phrase': ("Snyder's Moray",),
                'info': ({'name': 'It was discovered in 1904'},),
                'isLeaf': True
            },
            {
                'subject': ('eels', 'Zebra Moray'),
                'keywords': (('eel', 'snake-like'), ('zebra', 'striped', 'moray')),
                'phrase': ('Zebra Moray',),
                'info': ({'name': 'Diet', 'value': 'Sea urchins, mollusks, and crustaceans.'},),
                'isLeaf': True
            }
        ]
        self.assertEqual(flatten(resources, 0), res)

    def test_flatten_strip_duplicate_in_tree(self):
        resources2 = [
            {
                "name": "fishes",
                "keywords": ("fish seafood animal",),
                "phrase": ("It looks like you're looking for fishes.",),
                "options": ("What kind of fishes are you looking for?",),
                "children": (
                    {
                        "name": "deep sea fishes",
                        "keywords": ("deep bottom-dwellers",),
                        "phrase": ("We have several fishes that swim deep.",),
                        "children": [
                            {
                                "name": "Sword Fish",
                                # strip out this duplicate
                                "keywords": ("Sword Fish",),
                                "info": ({"name": "Unusual characteristics", "value": "sword"},),
                                "isLeaf": True,
                                "phrase": ("Sword Fish",),
                            }
                        ]
                    },
                )
            },
        ]
        res = [
            {
                'subject': ('fishes',),
                'keywords': (('fish', 'seafood', 'animal'),),
                'phrase': ("It looks like you're looking for fishes.",),
                'options': ('What kind of fishes are you looking for?',),
                'children': ('We have several fishes that swim deep.',)
            },
            {
                'subject': ('fishes', 'deep sea fishes'),
                'keywords': (('fish', 'seafood', 'animal'), ('deep', 'bottom-dweller')),
                'phrase': ('We have several fishes that swim deep.',),
                'children': ('Sword Fish',)
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Sword Fish'),
                'keywords': (('fish', 'seafood', 'animal'), ('deep', 'bottom-dweller'), ('sword',)),
                'phrase': ('Sword Fish',), 'info': ({'name': 'Unusual characteristics', 'value': 'sword'},),
                'isLeaf': True
            }
        ]
        self.assertEqual(flatten(resources2, 0), res)
