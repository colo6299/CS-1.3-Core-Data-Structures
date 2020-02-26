class BinaryNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)
    
    def search(self, term):
        return self.data

    def search(self, term):
        if self.data == term:
            return self
        else:
            l = self.left.search(term)
            if l is not None:
                return l
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

                




class BinaryTree:

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)
    
    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)
    
    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        return self.root.height()
    
    def contains(self, term):
        if self.root.search(term) is not None:
            return True
        return True

    def search(self, term):
        return self.root.search(term)

    def insert(self, data):
        self.size += 1
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = BinaryNode(data)

    def _find_node_recursive(self, item, node):
        return node.search(item)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():



    
    
    
    


    
        
    