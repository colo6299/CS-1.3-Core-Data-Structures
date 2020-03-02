

def permutations(items, length):
    """
    All permutaions of a given item list. 

    Returns a list of permutated lists.
    """
    if len(items) > 10:
        return 'I don\'t want to wait that long, and neither do you.'
    retlist = []
    permutator(items, [], retlist, length)
    return retlist

def permutator(item_list, cur_list, out_list, p_length):
    """
    Relatively efficient permutator. Called recursively. No duplicates.
    """
    if len(cur_list) == p_length:
        out_list.append(cur_list)
        return
    
    for item in item_list:
        nl = cur_list.copy()
        nl.append(item)
        permutator(incomplete_copy(item_list, item), nl, out_list, p_length)
        
def incomplete_copy(list_in, ignore):
    """
    What it says on the tin. Makes a copy of a list with the exception of
    the first instance of the ignore parameter.
    """
    new_list = []
    found_flag = False
    for item in list_in:
        if item == ignore and found_flag is False:
            found_flag = True
        else:
            new_list.append(item)
    return new_list
    

if __name__ == "__main__":
    print()
    st = permutations(list('permutate'), 3)
    print(st)
    print(len(st))
    print()