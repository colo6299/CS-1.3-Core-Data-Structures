#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item:
        return index
    if len(array) == index + 1:
        return None
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left_bound = 0
    right_bound = len(array) - 1
    count = 0
    #while (input() + 'k') is not None:

    loops = math.log2(len(array)) + 5 
    # note: doesn't seem to work reliably on lists of length >10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
    while count < loops:
        helta = int((right_bound + left_bound) / 2)
        #print(left_bound)
        #print(str(helta))
        #print(right_bound)
        if array[helta] > item:
            right_bound = helta
        elif array[helta] < item:
            left_bound = helta + 1
        elif array[helta] == item:
            print('\nIt\'s at index ', end='')
            print(helta)
            return helta
        count += 1

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left_bound=None, right_bound=None):
    # TODO: implement binary search iteratively here
    if left_bound is None:
        left_bound = 0
        right_bound = len(array) - 1

    l_old = left_bound
    r_old = right_bound
    # note: doesn't seem to work reliably on lists of length >10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
    helta = int((right_bound + left_bound) / 2)
    #print(left_bound)
    #print(str(helta))
    #print(right_bound)

    if array[helta] > item:
        right_bound = helta
    elif array[helta] < item:
        left_bound = helta + 1
    elif array[helta] == item:
        print('\nIt\'s at index ', end='')
        print(helta)
        return helta
    if (l_old == left_bound) and (r_old == right_bound):
        return
    return binary_search_recursive(array, item, left_bound, right_bound)
    


if __name__ == "__main__":
    print(binary_search_iterative(['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie'], 'Winnie'))