from q import ArrayQ
from ihop import IHOP_Array as stack

class CursedNode:
    # NOTE: I regret my choices in life
    def __init__(self, _next=None, data=None):
        self.next = _next
        self.data = data 

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def search(self, term):
        if self.data == term:
            return self
        else:
            if self.next.data is not None:
                l = self.next.data.search(term)
                if l is not None:
                    return l
            if self.next.next.data is not None:
                r = self.next.next.data.search(term)
                if r is not None:
                    return r

    def is_leaf(self):
        if (self.next.data is None and self.next.next.data is None):
            return True
        return False

    def is_branch(self):
        return not self.is_leaf()

    def height(self):
        left = 0
        right = 0
        if self.is_leaf():
            return 0
        if self.next.data is not None:
            left = self.next.data.height()
        if self.next.next.data is not None:
            right = self.next.next.data.height()   
        if left > right:
            return left + 1
        return right + 1

    def insert(self, data):
        if data < self.data:
            if self.next.data is not None:
                self.next.data.insert(data)
            else:
                self.next.data = CursedNode(CursedNode(CursedNode()), data)
        else:
            if self.next.next.data is not None:
                self.next.next.data.insert(data)
            else:
                self.next.next.data = CursedNode(CursedNode(CursedNode()), data)

    def set_insert(self, data):
        if data < self.data:
            if self.next.data is not None:
                self.next.data.insert(data)
            else:
                self.next.data = CursedNode(CursedNode(CursedNode()), data)
        elif data == self.data:
            self.data = data
            return True
        else:
            if self.next.next.data is not None:
                self.next.next.data.insert(data)
            else:
                self.next.next.data = CursedNode(CursedNode(CursedNode()), data)

    def items_pre_order(self, tree):
        tree.last_ordering.append(self.data)
        if self.next.data is not None:
            self.next.data.items_pre_order(tree)
        if self.next.next.data is not None:
            self.next.next.data.items_pre_order(tree)

    def items_in_order(self, tree):
        if self.next.data is not None:
            self.next.data.items_in_order(tree)
        tree.last_ordering.append(self.data)
        if self.next.next.data is not None:
            self.next.next.data.items_in_order(tree)

    def items_post_order(self, tree):
        if self.next.data is not None:
            self.next.data.items_post_order(tree)
        if self.next.next.data is not None:
            self.next.next.data.items_post_order(tree)
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
            if self.next.data is not None:
                l = self.next.data.search(term, self)
                if l is not None:
                    return l
            if self.next.next.data is not None:
                r = self.next.next.data.search(term, self)
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
            if self.next.data is not None:
                l = self.next.data.search(term)
                if l is not None:
                    return l
            if self.next.next.data is not None:
                r = self.next.next.data.search(term)
                if r is not None:
                    return r

    def predecessor(self, parent):
        if self.next.next.data is not None:
            return self.next.next.data.predecessor(self)
        self.delete(self)
        return parent, self

    # NOTE: I have elected to instead type this out every time.
    def binary_node_wink_wink(self, data, left=None, right=None, parent=None):
        return CursedNode(CursedNode(CursedNode(parent, right), left), data)
        

class CursedTree:
    """
    ALLTHESESQUARESMAKEACIRCLEALLTHESESQUARESMAKEACIRCLEALLTHESESQUARESMAKEACIRCLE
    """

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
        if self.root.search(term) is not None:
            return True
        return True

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
            self.root = CursedNode(CursedNode(CursedNode()), data)


    def set_insert(self, data):
        """
        O(log n) time
        """
        if self.root is not None:
            if self.root.set_insert(data):
                self.size += 1
        else:
            self.root = CursedNode(CursedNode(CursedNode()), data)
            self.size += 1

    def delete_old(self, item):
        if self.is_empty():
            raise KeyError
        node_tuple = self.root.find_parent_node_recursive_tuple(item).data
        self._delete_helper(node_tuple[1], node_tuple[0])

    def _delete_helper_old(self, node, parent):
        rlink = None
        if node.next.data is None:
            rlink = node.next.next.data
        if node.next.next.data is None:
            rlink = node.next.data
        pred = node.next.data.predecessor()
        pred[0].next.next.data = pred[1].next.data
        rlink = pred[1]
        if parent.data < node.data:
            parent.next.next.data = rlink
        else:
            parent.next.data = rlink

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
            if node.next.data is not None:
                queue.enqueue(node.next.data)
            if node.next.next.data is not None:
                queue.enqueue(node.next.next.data)

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
                if node.next.data is not None:
                    appender_stack.push(node.next.data)
                    visitor_stack.push(node.next.data)
            else:
                node = appender_stack.pop()
                items.append(node.data)
                if node.next.next.data is not None:
                    appender_stack.push(node.next.next.data)
                    visitor_stack.push(node.next.next.data)
        return items