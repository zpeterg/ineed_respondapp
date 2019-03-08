
from .similarity import similarity


def parsePhrase(arr, synomized_phrase):
    rtn = {'count': 0, 'similarity': 0, 'lastCount': 0, 'lastSimilarity': 0, 'matching': ()}
    last_count = 0
    last_similarity = 0
    # prep each piece of comparison array
    for x in arr:
        sim = similarity(x, synomized_phrase)
        # get count of matching phrases
        rtn['similarity'] += sim['count']
        last_similarity = sim['count']
        # get total similarity (can match multiple parts of each phrase in 'arr'
        if sim['count'] > 0:
            rtn['count'] += 1
            last_count = 1
            rtn['matching'] += sim['matching']
        else:
            last_count = 0
    rtn['lastCount'] = last_count
    rtn['lastSimilarity'] = last_similarity
    return rtn
