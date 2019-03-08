from .parsePhrase import parsePhrase
from .fragIt import fragIt
from .cleanIt import cleanIt
from .synomize import synomize

def prepPhrase(phrase):
    return cleanIt(fragIt(phrase))

def match_to_list(tup, search_str):
    highest_similarity = {'similarity': 0, 'count': 0, 'lastCount': 0, 'lastSimilarity': 0, 'matching': ()}
    highest_similarity_item = tup[0]
    synomized_phrase = synomize(prepPhrase(search_str))

    for item in tup:
        # parsePhrase() returns something like {'count': 2, 'similarity': 3, 'lastCount': 0, 'lastSimilarity': 0}
        sim = parsePhrase(item['keywords'], synomized_phrase)
        # only count as highest similarity if has highest match, AND matches on the last item
        if highest_similarity['count'] < sim['count'] and sim['lastCount'] > 0:
            highest_similarity_item = item
            highest_similarity = sim
    return {
        'count': highest_similarity['count'],
        'similarity': highest_similarity['similarity'],
        'value': highest_similarity_item,
        'lastCount': highest_similarity['lastCount'],
        'lastSimilarity': highest_similarity['lastSimilarity'],
        'matching': highest_similarity['matching'],
    }


class Chat:
    def __init__(self, flattened_res, subject, language=0):
        self.flattened_res = flattened_res
        self.subject = subject
        self.language = language

    def match(self, search_str):
        all_matching = ()
        level_matching = ()
        most_sim = None
        for item in self.flattened_res:
            # Merge subjects into strings, and look to see if the subject sought is in this item's subject
            if ''.join(self.subject) in ''.join(item['subject']):
                all_matching += (item,)
                # If next level-deep, add to that list
                if len(self.subject) + 1 == len(item['subject']):
                    level_matching += (item,)
        # If some next-level items, check those
        if len(level_matching) != 0:
            # Match to items that share subject (sub-tree)
            most_sim = match_to_list(level_matching, search_str)
        # If next-level doesn't match, check everything down-tree
        if (not most_sim or most_sim['count'] <= 0) and len(all_matching) != 0:
            most_sim = match_to_list(all_matching, search_str)
        # If nothing matches down-tree, look everywhere
        if not most_sim or most_sim['count'] <= 0:
            most_sim = match_to_list(self.flattened_res, search_str)
        # Adjust certainty on total matching or match count
        # certainty is 0-2
        if len(all_matching) == 0:
            certainty = 2
        elif most_sim['count'] < 1:
            certainty = 0
        else:
            certainty = 1

        if most_sim:
            most_sim['certainty'] = certainty
        return most_sim
