

def is_valid(text, term):
    if len(text) == 0:
        return False

def substring_in(text, term):
    if term == '':
        return 0
    if is_valid(text, term) is False:
        return 
    for i in range(len(text)):
        if text[i] == term[0]:
            ndx = search_jenga(text, term, i)
            if ndx is not None:
                return ndx
    return

def substring_all(text, term):
    retlist = []
    if term == '':
        return list(range(len(text)))
    if is_valid(text, term) is False:
        return 
    for i in range(len(text)):
        if text[i] == term[0]:
            ndx = search_jenga(text, term, i)
            if ndx is not None:
                retlist.append(ndx)
    return retlist

def search_jenga(text, term, index):
    for j in range(len(term)):
        if (index + j) > len(text) - 1:
            return
        if term[j] != text[index + j]:
            return
    return index

def hybrid_s3(text, term):
    associator_dict = {}

    #build associator dict entries
    for char in term:
        associator_dict[char] = list()
    '''
    for 
    top_index = len(text) - len(term)
    shift = 0
    '''
