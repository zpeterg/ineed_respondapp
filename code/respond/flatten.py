from .fragIt import fragIt
from .cleanIt import cleanIt

def prepPhrase(phrase):
    rtn = cleanIt(fragIt(phrase))
    return rtn

def clean_child(parent_keywords, keywords):
    # convert to array to make mutable
    keywords_arr = list(keywords)
    # strip out all the words that appear in parents
    for words in parent_keywords:
        for word in words:
            if word in keywords_arr:
                del keywords_arr[keywords_arr.index(word)]
    # convert back to tuple
    return tuple(keywords_arr)


def flatten(resources, language=0):
    rtn = []

    def loop(level, parent_names, parent_keywords):
        for item in level:
            subject = parent_names + (item['name'],)
            keywords = prepPhrase(item['keywords'][language])
            keywords = clean_child(parent_keywords, keywords)
            keywords = parent_keywords + (keywords,)
            new_item = {
                "subject": subject,
                "keywords": keywords,
            }
            if 'phrase' in item:
                new_item['phrase'] = item['phrase']
            if 'options' in item:
                new_item['options'] = item['options']
            if 'info' in item:
                new_item['info'] = item['info']
            if 'isLeaf' in item:
                new_item['isLeaf'] = item['isLeaf']
            if 'children' in item:
                children = ()
                for c in item['children']:
                    children += (c['phrase'][language],)
                new_item['children'] = children
            # Add that item
            rtn.append(new_item)
            # Move into the children and loop them
            if 'children' in item:
                loop(item['children'], subject, keywords)

    loop(resources, (), ())
    return rtn
