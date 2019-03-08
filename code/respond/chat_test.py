import unittest
from .chat import match_to_list, Chat
from .flatten import flatten

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


class TestChat(unittest.TestCase):
    def test_match_to_list(self):
        tup = (
            {'keywords': ('fish seafood animal',)},
            {'keywords': ('fish seafood animal', 'deep bottom-dwellers')},
            {'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Angler Lophiiformes')},
            {'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Sword Xiphias')},
        )
        res = {
            'count': 2,
            'lastCount': 1,
            'lastSimilarity': 1,
            'matching': ('fish', 'deep'),
            'similarity': 2,
            'value': tup[1],
        }
        phrase = 'fishs that swim down deep'
        returned = match_to_list(tup, phrase)
        self.assertEqual(returned, res)

    def test_chat_constructor(self):
        resources = [{'name': 'foo', 'keywords': ('foo man',)}]
        subject = ['bar']
        thisChat = Chat(resources, subject)
        self.assertEqual(resources, thisChat.flattened_res)
        self.assertEqual(subject, thisChat.subject)

    def test_chat_match(self):
        search_str = 'Angler'
        res = {
            'count': 1,
            'lastCount': 1,
            'lastSimilarity': 1,
            'matching': ('angler',),
            'similarity': 1,
            'value': {
                'subject': ('fishes', 'deep sea fishes', 'Angler Fish'),
                'keywords': (('fish', 'seafood', 'animal'), ('deep', 'bottom-dweller'), ('angler', 'lophiiformes')),
                'phrase': ('Angler Fish',),
                'info': ({'name': 'It has a light'},),
                'isLeaf': True
            },
            'certainty': 1
        }
        thisChat = Chat(flatten(resources), ['fishes', 'deep sea fishes'])
        self.assertEqual(thisChat.match(search_str), res)

    def test_chat_match_alternative(self):
        search_str = 'Zebra'
        res = {
            'count': 1,
            'similarity': 1,
            'value': {
                'subject': ('eels', 'Zebra Moray'),
                'keywords': (('eel', 'snake-like'), ('zebra', 'striped', 'moray')),
                'phrase': ('Zebra Moray',),
                'info': ({'name': 'Diet', 'value': 'Sea urchins, mollusks, and crustaceans.'},),
                'isLeaf': True
            },
            'lastCount': 1,
            'lastSimilarity': 1,
            'matching': ('zebra',),
            'certainty': 2
        }

        thisChat = Chat(flatten(resources), ['fishes', 'nothingthere'])
        self.assertEqual(thisChat.match(search_str), res)

    def test_chat_match_prefer_up_tree(self):
        resources2 = [
            {
                "name": "counseling",
                "keywords": ("counseling",),
                "phrase": ("About counseling",),
                "options": ("What counseling are you looking for?",),
                "children": (
                    {
                        "name": "Guidance",
                        "keywords": ("guidance",),
                        "info": (),
                        "isLeaf": True,
                        "phrase": ("Guidance Service",),
                    },
                )
            },
        ]
        search_str = 'counseling'
        res = {
            'count': 1,
            'similarity': 2,
            'value': {'subject': ('counseling',), 'keywords': (('counseling',),), 'phrase': ('About counseling',), 'options': ('What counseling are you looking for?',), 'children': ('Guidance Service',)},
            'lastCount': 1,
            'lastSimilarity': 2,
            'matching': ('counseling', 'counseling'),
            'certainty': 1,
        }

        thisChat = Chat(flatten(resources2), ())
        self.assertEqual(thisChat.match(search_str), res)
