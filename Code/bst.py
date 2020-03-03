from q import ArrayQ
from ihop import IHOP_Array as stack

class BinaryNode:
    # NOTE: all of the big O stuff is on the tree class :)
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def search(self, term):
        if self.data == term:
            return self
        else:
            if term < self.data:
                if self.left is not None:
                    l = self.left.search(term)
                    if l is not None:
                        return l
            else:
                if self.right is not None:
                    r = self.right.search(term)
                    if r is not None:
                        return r

    def is_leaf(self):
        if (self.left is None and self.right is None):
            return True
        return False

    def is_branch(self):
        return not self.is_leaf()

    def height(self):
        left = 0
        right = 0
        if self.is_leaf():
            return 0
        if self.left is not None:
            left = self.left.height()
        if self.right is not None:
            right = self.right.height()   
        if left > right:
            return left + 1
        return right + 1

    def insert(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BinaryNode(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BinaryNode(data)

    def set_insert(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BinaryNode(data)
        elif data == self.data:
            self.data = data
            return True
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BinaryNode(data)

    def items_pre_order(self, tree):
        tree.last_ordering.append(self.data)
        if self.left is not None:
            self.left.items_pre_order(tree)
        if self.right is not None:
            self.right.items_pre_order(tree)

    def items_in_order(self, tree):
        if self.left is not None:
            self.left.items_in_order(tree)
        tree.last_ordering.append(self.data)
        if self.right is not None:
            self.right.items_in_order(tree)

    def items_post_order(self, tree):
        if self.left is not None:
            self.left.items_post_order(tree)
        if self.right is not None:
            self.right.items_post_order(tree)
        tree.last_ordering.append(self.data)

    def find_parent_node_recursive(self, term, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""

        if self.data == term:
            return parent
        else:
            if self.left is not None:
                l = self.left.search(term, self)
                if l is not None:
                    return l
            if self.right is not None:
                r = self.right.search(term, self)
                if r is not None:
                    return r

    def find_parent_node_recursive_tuple(self, term, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""

        if self.data == term:
            return (parent, self)
        else:
            if self.left is not None:
                l = self.left.find_parent_node_recursive_tuple(term, self)
                if l is not None:
                    return l
            if self.right is not None:
                r = self.right.find_parent_node_recursive_tuple(term, self)
                if r is not None:
                    return r

    def predecessor(self, parent=None):
        if self.right is not None:
            return self.right.predecessor(self)
        return parent, self
        

class BinaryTree:

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        self.last_ordering = []
        if items is not None:
            for item in items:
                self.insert(item)
    
    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)
    
    def is_empty(self):
        """ O(1)
        Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """
        O(1)
        """
        return self.root.height()
    
    def contains(self, term):
        """
        O(log n) time
        """
        if self.search(term) is not None:
            return True
        return False

    def _find_parent_node_recursive(self, term):
        """O(log n)
        Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        if self.is_empty() is not True:
            return self.root.find_parent_node_recursive(term)

    def search(self, term):
        """
        O(log n) time
        """
        node = self.root.search(term)
        if node is not None:
            return node.data

    def insert(self, data):
        """
        O(log n) time
        """
        self.size += 1
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = BinaryNode(data)

    def set_insert(self, data):
        """
        O(log n) time
        """
        if self.root is not None:
            if self.root.set_insert(data):
                self.size += 1
        else:
            self.root = BinaryNode(data)
            self.size += 1

    def delete(self, item):
        parent_child_nodes = self.root.find_parent_node_recursive_tuple(item)
        parent_node = parent_child_nodes[0]
        delete_node = parent_child_nodes[1]
        left_bool = False
        if parent_node is not None:
            if parent_node.left == delete_node:
                left_bool = True

        if delete_node.left is not None and delete_node.right is not None:
            pred = delete_node.left.predecessor()
            retnode = pred[1]
            if pred[0] is not None:
                pred[0].right = pred[1].left
                pred[1].right = delete_node.right
                pred[1].left = delete_node.left
            else:
                pred[1].right = delete_node.right
            
        elif delete_node.left is not None:
            retnode = delete_node.left
        elif delete_node.right is not None:

            retnode = delete_node.right
        else:
            retnode = None

        if parent_node is None:
            self.root = retnode
        elif left_bool:
            parent_node.left = retnode
        else:
            parent_node.right = retnode

    def _find_node_recursive(self, item, node):
        """
        O(log n) time
        """
        return node.search(item)

    def items_level_order(self):
        """O(n) time and space
        Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """ O(n) time and space
        Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        queue = ArrayQ()
        queue.enqueue(start_node)
        while queue.is_empty() is not True:
            node = queue.dequeue()
            visit(node.data)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

    def items_pre_order(self):
        """
        O(n) time, O(log n) space
        Return a pre-order list of all items in this binary search tree."""
        self.last_ordering = []
        if True:
            self.root.items_pre_order(self)
        return self.last_ordering

    def items_in_order(self):
        """
        O(n) time, O(log n) space
        Return a pre-order list of all items in this binary search tree."""
        self.last_ordering = []
        if True:
            self.root.items_in_order(self)
        return self.items_in_order_iterative()

    def items_post_order(self): 
        """
        O(n) time, O(log n) space
        Return a pre-order list of all items in this binary search tree."""
        self.last_ordering = []
        if True:
            self.root.items_post_order(self)
        return self.last_ordering

    def items_in_order_iterative(self):
        """
        O(n) time, O(log n) space
        """
        if self.is_empty(): 
            return []
        appender_stack = stack([self.root])
        visitor_stack = stack([self.root])
        items = []

        while appender_stack.is_empty() is False:
            if visitor_stack.is_empty() is False:
                node = visitor_stack.pop()
                if node.left is not None:
                    appender_stack.push(node.left)
                    visitor_stack.push(node.left)
            else:
                node = appender_stack.pop()
                items.append(node.data)
                if node.right is not None:
                    appender_stack.push(node.right)
                    visitor_stack.push(node.right)
        return items
        
    def items_pre_order_iterative(self):
        """
        O(n) time, O(log n) space
        """
        if self.is_empty(): 
            return []
        appender_stack = stack([self.root])
        visitor_stack = stack([self.root])
        items = []

        while appender_stack.is_empty() is False:
            if visitor_stack.is_empty() is False:
                node = visitor_stack.pop()
                if node.left is not None:
                    items.append(node.data)
                    appender_stack.push(node.left)
                    visitor_stack.push(node.left)
            else:
                node = appender_stack.pop()
                if node.right is not None:
                    items.append(node.data)
                    appender_stack.push(node.right)
                    visitor_stack.push(node.right)
        return items

    def items_post_order_iterative(self):
        """
        O(n) time, O(log n) space
        """
        if self.is_empty(): 
            return []
        appender_stack = stack([self.root])
        visitor_stack = stack([self.root])
        items = []

        while appender_stack.is_empty() is False:
            if visitor_stack.is_empty() is False:
                node = visitor_stack.pop()
                if node.left is not None:
                    items.append(node.data)
                    appender_stack.push(node.left)
                    visitor_stack.push(node.left)
            else:
                node = appender_stack.pop()
                if node.right is not None:
                    appender_stack.push(node.right)
                    visitor_stack.push(node.right)
        return items


from hash_browns import Hashbrowns as Hashtable
from recomper import Combinator
from recomper import Permutator
import cProfile
import sys
import json

def dejumbler(jumble, meltionary):
    melty_word = word_melter(jumble)
    valid_list = []

    if melty_word not in meltionary:
        return valid_list

    for valid_word in meltionary[melty_word]:
        if is_letter_list_permutation(valid_word, jumble):
            valid_list.append(valid_word)
    return valid_list

def multi_dejumble(jumble_letters, word_lengths, meltionary):

    retlist = []
    for num in word_lengths:
        retlist.append([])
    _multi_word_dejumbler(list(jumble_letters), word_lengths, [], retlist, meltionary)
    return retlist

# out_list should be a list of empty list of length len(word_lengths) i.e. [2, 6] -> [ [], [] ] ->
#                                                    -> the result is a list of solutions of length [1, 2]
def _multi_word_dejumbler(jumble_letters, word_lengths, cur_words, out_list, d, _ndx=-1):   

    c = Combinator()
    _ndx += 1
    if _ndx == len(word_lengths):
        return
    for combo, compliment in c.combo_compliments(jumble_letters, word_lengths[_ndx]):
        valid_words = dejumbler(combo, d)
        if len(valid_words) == 0:
            if len(cur_words) != 0:
                let_list = list(cur_words)
                longth = len(cur_words)
                str_comp = ''.join(jumble_letters)
                let_list.append(str_comp)
                out_list[len(word_lengths) - longth].append(let_list)
        for valid_word in valid_words:
            new_words = list(cur_words)
            new_words.append(valid_word)
            _multi_word_dejumbler(compliment, word_lengths, new_words, out_list, d, _ndx)

def dictionary_melter():
    f = open('big_dict.txt')
    table = Hashtable()

    index = -1
    while True:
        index += 1
        word = f.readline()
        word = word.strip().lower()
        if word is '':
            f.close()
            return table
        melty = word_melter(word)
        if melty in table:
            table.get(melty).append(word)
        else:
            table.set(melty, [word])

def dictionary_melter_std():
    """
    I know using the pythomn dict is kind of cheating, but I've 
    had enough of serialization ever since I got into Unity
    """
    f = open('big_dict.txt')
    table = {}

    index = -1
    while True:
        index += 1
        word = f.readline()
        word = word.strip().lower()
        if word is '':
            f.close()
            return table
        melty = word_melter(word)
        if melty in table:
            table[melty].append(word)
        else:
            table[melty] = [word]

def word_melter(word):
    letter_array = [None] * 27  # 27 is dash (-)
    for letter in word:
        if letter == '-':
            letter_array[26] = True
        else:
            letter_array[ord(letter) - 97] = True
    retstring = ''
    for index, letter in enumerate(letter_array):
        if letter is True:
            retstring += chr(index + 97)
    return retstring

def is_letter_list_permutation(llist_1, llist_2):
    
    if len(llist_1) != len(llist_2):
        return False

    fraction_l1 = [0] * 27
    fraction_l2 = [0] * 27
    for letter in llist_1:
        fraction_l1[ord(letter) - 97] += 1
    for letter in llist_2:
        fraction_l2[ord(letter) - 97] += 1

    if fraction_l1 == fraction_l2:
        return True
    else:
        return False

def meltionary_writer(meltionary):
    dd = json.dumps(meltionary)
    f = open("meltionary.json","w")
    f.write(dd)
    f.close()

def meltionary_reader():
    f = open("meltionary.json","r")
    ds = json.load(f)
    f.close()
    return ds

def jumble_runner(meltionary):
     
    primary_jumbles = [
        ['tefon', '--o-o'],
        ['sokik', 'oo-o-'],
        ['niumem', '----o-'],
        ['siconu', '---oo-']
    ]

    answers = []
    for jumble in primary_jumbles:
        answers.append(dejumbler(jumble[0], meltionary))

    secondary_word_lengths = [6, 2]
    secondary_letters = ''
    for ndx, jumble in enumerate(primary_jumbles):
        for index, letter in enumerate(jumble[1]):
            if letter == 'o':
                secondary_letters += answers[ndx][0][index]

    secondary_answers_list = multi_dejumble(secondary_letters, secondary_word_lengths, meltionary)

    
    print()
    print(answers)
    print()
    print(secondary_answers_list[1])
    print()

    return (answers, secondary_answers_list)

def trash():
    """
    Just waiting for the garbageman
    """
    """
    c = Combinator()
    combos = c.combinations(list(secondary_letters), seondary_jumble[0])
    possible_secondary_answers = []
    for combo in combos:

        
        compliment = c.compliment(combo, list(secondary_letters))
        combo = word_melter(''.join(combo))
        compliment = word_melter(''.join(compliment))

        answer_1 = dejumbler(combo, meltionary)
        answer_2 = dejumbler(compliment, meltionary)

        if len(answer_1) is not 0 and len(answer_2) is not 0:
            possible_secondary_answers.append((answer_1, answer_2))

    probable_secondary_answers = []
    for possible_answer in possible_secondary_answers:
        probable_secondary_answers.append(possible_answer) 
    """

if __name__ == "__main__":

    #cProfile.run('dictionary_melter()')
    d = dictionary_melter_std()
    meltionary_writer(d)
    d = meltionary_reader()
    #meltionary_writer(d)
    #cProfile.run('jumble_runner(d)')
    jumble_runner(d)
    #print(dejumbler('short', d))  # sardine


        

                
        
        