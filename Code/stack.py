#!python

from linkedlist import LinkedList

class Node:
    def __init__(self, next=None, data=None):
        self.next
        self.data

class LinkedList:
    def __init__(self, starter_list=None):
        self.length = 0
        self.head
        self.tail

        for item in starter_list:
            pass
    
    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def length(self):
        return self.count

    def append(self, item):
        pass

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests

# Stack = ArrayStack
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

Stack = IHOP_LL