from lonkedlist import LonkedList as LonkedList


class IHOP_LL(object):   

    def __init__(self, iterable=None):
        self.list = LonkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def length(self):  # O(1)
        return self.list.length()

    def is_empty(self):  # O(1)
        if self.length() > 0:
            return False
        return True

    def push(self, item):  # O(1)
        self.list.prepend(item)

    def peek(self):  # O(1)
        if self.is_empty():
            return
        return self.list.head.data

    def pop(self):  # O(1)
        if self.is_empty():
            raise ValueError
        data = self.list.head.data  
        self.list.delete(self.list.head.data)
        return data

class IHOP_Array(object):   

    def __init__(self, iterable=None):
        self.list = []
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def length(self):  # O(1)
        return len(self.list)

    def is_empty(self):  # O(1)
        if self.length() > 0:
            return False
        return True

    def push(self, item):  # O(1)
        self.list.append(item)

    def peek(self):  # O(1)
        if len(self.list) > 0:
            return self.list[-1]
        return 

    def pop(self):  # O(1)
        if self.is_empty():
            raise ValueError
        return self.list.pop()

