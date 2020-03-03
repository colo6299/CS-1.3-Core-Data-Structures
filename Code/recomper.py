import cProfile

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

    def _permutator(self, item_list, cur_list, out_list, p_length):
        """
        Relatively efficient permutator. Called recursively.
        """
        if len(cur_list) == p_length:
            out_list.append(cur_list)
            return
        
        for item in item_list:
            nl = cur_list.copy()
            nl.append(item)
            self._permutator(self.incomplete_copy(item_list, item), nl, out_list, p_length)
            
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

    def combo_compliments(self, items, length):
        retlist = []
        self._complimator(items, [False] * len(items), 0, retlist, length)
        return retlist
    
    def compliment(self, cur_list, list_in):
        retlist = []
        for item in list_in:
            if item not in cur_list:
                retlist.append(item)
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

    def _complimator(self, item_list, cur_list, item_ndx, out_list, p_length):

        if sum(cur_list) == p_length:
            
            combination = []
            compliment = []
            for index, add in enumerate(cur_list):
                if add is True:
                    combination.append(item_list[index])
                else:
                    compliment.append(item_list[index])

            out_list.append((combination, compliment))
            return
        elif item_ndx > len(item_list) - p_length + sum(cur_list):
            return

        affirmative_list = list(cur_list)
        affirmative_list[item_ndx] = True
        self._complimator(item_list, affirmative_list, item_ndx + 1, out_list, p_length)
        self._complimator(item_list, list(cur_list), item_ndx + 1, out_list, p_length)

def test_permutation():
    p = Permutator()

    ls = p.permutations([1, 2, 3, 4, 5], 5)
    assert len(ls) == 120
    assert [3, 2, 1, 4, 5] in ls
    
    ls = p.permutations([1, 2, 3, 4, 5, 6, 7], 4)
    assert len(ls) == 840
    assert [7, 4, 3, 6] in ls

    ls = p.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    assert len(ls) == 10
    assert [7] in ls

def test_combination():
    c = Combinator()

    ls = c.combinations([1, 2, 3, 4, 5], 5)
    assert len(ls) == 1
    assert [1, 2, 3, 4, 5] in ls
    
    ls = c.combinations([1, 2, 3, 4, 5, 6, 7], 4)
    assert len(ls) == 35
    assert [3, 4, 6, 7] in ls  # a quirk of generation ensures an ordered product

    ls = c.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    assert len(ls) == 10
    assert [7] in ls

if __name__ == "__main__":
    #cermutator = Permutator()
    #cProfile.run('cermutator.permutations(list(\'permutate\'), 9)')
    #print(st)
    pass
    