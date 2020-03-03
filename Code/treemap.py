from bst import BinaryNode, BinaryTree

class KeyValuePackage(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __getitem__(self, index):
        if index == 0:
            return self.key
        elif index == 1:
            return self.value
        elif index == 2:
            return self.key, self.value
        else:
            raise IndexError

    def __repr__(self):
        return str('(' + str(self.key) + ', ' + str(self.value) + ')')

    def __lt__(self, value):
        return self.key < value
    
    def __gt__(self, value):
        return self.key > value

    def __eq__(self, value):
        return self.key == value

class TreeMap:

    def __init__(self):
        self.tree = BinaryTree()
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of cursed tree map."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this cursed tree map."""
        return 'TreeMap({!r})'.format(self.items())

    def items(self):
        items = self.tree.items_in_order()
        retlist = []
        for item in items:
            retlist.append((item.key, item.value))
        return retlist

    def keys(self):
        items = self.tree.items_in_order()
        for item in items:
            yield item.key

    def set(self, key, value):
        self.tree.set_insert(KeyValuePackage(key, value))

    def get(self, key):
        return self.tree.search(key).value

    def contains(self, key):
        return self.tree.contains(key)

    def delete(self, key):
        self.tree.delete(key)



def test_treemap():
    t = TreeMap()
    t.set('I', 11)
    t.set('P', 'asdadf')
    t.set('I', 12)
    t.set('j', 12)
    t.set('1', 12)
    t.set('6', 12)
    t.set('y', 12)
    t.set('a', 12)
    t.set('b', 12)

    assert t.contains('y') == True
    assert t.contains('6') == True

    t.delete('6')
    t.delete('I')

    assert t.contains('6') == False
    assert t.contains('11334') == False

if __name__ == "__main__":
    t = TreeMap()
    t.set('I', 11)
    t.set('P', 'asdadf')
    t.set('I', 12)
    t.set('j', 12)
    t.set('1', 12)
    t.set('6', 12)
    t.set('y', 12)
    t.set('a', 12)
    t.set('b', 12)
    t.delete('6')
    t.delete('I')
    print(t.contains('I'))
    print(t.tree.search('I'))
    assert t.contains('I') == False
    print(t.tree.items_pre_order())

