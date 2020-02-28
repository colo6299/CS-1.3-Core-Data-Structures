from lonkedlist import LonkedList

class LinkedQ:

    def __init__(self, iterable=None):
        self.list = LonkedList()

        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def __iter__(self):
        for item in self.list:
            yield item

    def is_empty(self):
        if self.length() > 0:
            return False
        return True

    def length(self):
        return self.list.length()

    def front(self):
        if self.length() > 0:
            return self.list.head.data
        return

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError
        data = self.list.head.data  
        self.list.delete(self.list.head.data)
        return data
    
class ArrayQ: 
    def __init__(self, iterable=None):
        self.list = []

        if iterable:
            for item in iterable:
                self.enqueue(item)   

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def __iter__(self):
        for item in self.list:
            yield item

    def is_empty(self):
        if self.length() > 0:
            return False
        return True

    def length(self):
        return len(self.list)

    def front(self):
        if self.length() > 0:
            return self.list[0]
        return

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError
        return self.list.pop(0)

class ArrayDeque: 
    def __init__(self, iterable=None):
        self.list = []

        if iterable:
            for item in iterable:
                self.enqueue(item)   

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def __iter__(self):
        for item in self.list:
            yield item

    def is_empty(self):
        """
        O(1)
        """
        if self.length() > 0:
            return False
        return True

    def length(self):
        """
        O(1)
        """
        return len(self.list)

    def front(self):
        """
        O(1)
        """
        if self.length() > 0:
            return self.list[0]
        return

    def back(self):
        """
        O(1)
        """
        if self.length() > 1:
            return self.list[-1]
        if self.length() == 1:
            return self.list[0]
        return

    def push_back(self, item):
        """
        O(1)
        """
        self.list.append(item)
    
    def push_front(self, item):
        """
        O(n)
        """
        self.list.insert(0, item)  # suck it, guido

    def pop_front(self):
        """
        O(n)
        """
        if self.is_empty():
            raise ValueError
        return self.list.pop(0)

    def pop_back(self): 
        """
        O(1)
        """
        if self.is_empty():
            raise ValueError
        if self.length == 1:
            return self.list.pop(0)
        return self.list.pop(-1)
    