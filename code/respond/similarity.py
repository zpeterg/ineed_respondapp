
def similarity(arr, syno_phrase):
    rtn = {'count': 0, 'syn_count': 0, 'matching': ()}
    for synos in syno_phrase:
        syn_count = 0
        for syno in synos:
            if syno in arr:
                rtn['matching'] += (syno,)
                syn_count += 1
        rtn['syn_count'] += syn_count
        # Only plus-up the 'count' on a word (syn collection)-basis
        if syn_count > 0:
            rtn['count'] += 1
    return rtn

