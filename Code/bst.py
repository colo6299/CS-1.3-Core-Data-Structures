from q import ArrayQ
from ihop import IHOP_Array as stack

class BinaryNode:

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
            if self.left is not None:
                l = self.left.search(term)
                if l is not None:
                    return l
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
            return parent, self
        else:
            if self.left is not None:
                l = self.left.search(term, self)
                if l is not None:
                    return l
            if self.right is not None:
                r = self.right.search(term, self)
                if r is not None:
                    return r

    def predecessor(self):
        if self.right is not None:
            return predecessor(self.right)
        self.delete(self)
        return self
        
    
        
                




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
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        return self.root.height()
    
    def contains(self, term):
        if self.root.search(term) is not None:
            return True
        return True

    def _find_parent_node_recursive(self, term):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        if self.is_empty() is not True:
            return self.root.find_parent_node_recursive(term)

    def search(self, term):
        node = self.root.search(term)
        if node is not None:
            return node.data

    def insert(self, data):
        self.size += 1
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = BinaryNode(data)

    def _find_node_recursive(self, item, node):
        return node.search(item)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
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
        """Return a pre-order list of all items in this binary search tree."""
        self.last_ordering = []
        if True:
            self.root.items_pre_order(self)
        return self.last_ordering

    def items_in_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        self.last_ordering = []
        if True:
            self.root.items_in_order(self)
        return self.items_in_order_iterative()

    def items_post_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        self.last_ordering = []
        if True:
            self.root.items_post_order(self)
        return self.last_ordering

    def items_in_order_iterative(self):
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
        
            
                
        
        