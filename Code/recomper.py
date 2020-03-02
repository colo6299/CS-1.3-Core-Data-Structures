
class Permutator:

    def permutations(self, items, length):
        """
        All permutaions of a given item list. 

        Returns a list of permutated lists.
        """
        if len(items) > 10:
            return 'I don\'t want to wait that long, and neither do you.'
        retlist = []
        self._permutator(items, [], retlist, length)
        return retlist

    def permutator(self, item_list, cur_list, out_list, p_length):
        """
        Relatively efficient permutator. Called recursively. No duplicates.
        """
        if len(cur_list) == p_length:
            out_list.append(cur_list)
            return
        
        for item in item_list:
            nl = cur_list.copy()
            nl.append(item)
            self._permutator(incomplete_copy(item_list, item), nl, out_list, p_length)
            
    def incomplete_copy(self, list_in, ignore):
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
        

class Combinator:

    def combinations(self, items, length):
        """
        A-Plus _nice_ combination maker-inator. 

        Returns a list of combinated lists.
        """
        retlist = []
        self._combinator(items, [], 0, retlist, length)
        return retlist
        

    def _combinator(self, item_list, cur_list, item_ndx, out_list, p_length):
        """
        Honestly, this docstring is mostly for style points.

        The function's pretty good too, though.
        """
        if len(cur_list) == p_length:
            out_list.append(cur_list)
            return
        elif item_ndx > len(item_list) - p_length + len(cur_list):
            return 

        affirmative_list = list(cur_list)
        affirmative_list.append(item_list[item_ndx])
        self._combinator(item_list, affirmative_list, item_ndx + 1, out_list, p_length)
        self._combinator(item_list, list(cur_list), item_ndx + 1, out_list, p_length)

if __name__ == "__main__":
    combine = Combinator()
    st = combine.combinations(list('combinate'), 4)
    print(st)
    print(len(st))