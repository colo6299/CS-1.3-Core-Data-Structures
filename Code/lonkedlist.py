class Node(object):
    def __init__(self, data = None, next_node = None):
        self.next = next_node
        self.data = data

class LonkedList(object):
    def __init__(self, init_list = None, start_length = 0, default_data = None):
        self.count = 0
        self.head = None
        self.tail = None
        self.size = 0

        if init_list == None:
            init_list = []

        for i in init_list:
            self.append(i)

    def is_empty(self):
        '''
        Always O(1), just returning a bool, here
        '''
        return bool(self.head)

    def items(self, process=lambda data: data):
        '''
        Always O(n), c'mon, what'd you expect? 

        pass a lambda process for fun & profit
        '''
        retlist = []
        node = self.head
        while node is not None:
            retlist.append(process(node.data))
            node = node.next
        return retlist
    
    def append(self, data):
        '''
        Always O(1), it's just plopped in back
        '''
        new_node = Node(data)
        self.count += 1
        self.size += 1
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, data):
        '''
        Always O(1), it's just plopped in front
        '''
        new_node = Node(data, self.head)
        self.count += 1
        self.size += 1
        if self.tail != None:
            self.head = new_node 
        else:
            self.head = new_node
            self.tail = new_node
    
    def length(self):
        '''
        Always O(1), we're literally just returning a number here
        '''
        return self.count

    def absolute_length(self):
        '''
        Always O(n), linear counter. Definitely correct. 
        '''
        node = self.head
        count = 0
        while node != None:
            node = node.next
            count += 1
        self.count = count
        self.size = count

    def get_at_index(self, index):
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        node = self.head
        count = 0
        while node is not None and (count < index):
            node = node.next
            count += 1
        if node is not None:
            return node.data

    def insert_at_index(self, index, data):
        node = self.head
        count = 0
        new_node = Node(data)

        if index > self.length():
            raise IndexError

        self.count += 1
        self.size += 1
        
        while node is not None and (count < index - 1):
            node = node.next
            count += 1

        if index == self.length():
            self.tail = new_node
        
        if index == 0:
            self.head == new_node

        if node is not None:
            new_node.next = node.next
            node.next = new_node




    def find(self, quality):
        '''
        '''
        node = self.head
        while node != None:
            if quality(node.data):
                return node.data
            node = node.next
        #return False

    def replace(self, finda, data):
        '''
        '''
        node = self.head
        while node != None:
            if node.data == finda:
                node.data = data
                return
            node = node.next
        raise ValueError
        
        #return False

    def old_find(self, item):
        '''
        O(n) average/worst case, O(1) best case if the item is contained
        in the first node.
        '''
        node = self.head
        while node != None:
            if node.data == item:
                return node.data
            node = node.next
        #raise ValueError

    def delete(self, item=None, quality=None):
        '''
        O(n) average/worst case, O(1) best case if the item is contained
        in the first node.
        '''
        p_node = None
        node = self.head
        while node != None:
            if quality is not None:
                if quality(node.data):
                    if node == self.tail:
                        self.tail = p_node
                    if node != self.head:
                        p_node.next = node.next
                        self.count -= 1
                        self.size -= 1
                        return #d4ful
                    else:
                        self.head = node.next
                        self.count -= 1
                        self.size -= 1
                        return #d4ful

            elif node.data == item:
                if node == self.tail:
                    self.tail = p_node
                if node != self.head:
                    p_node.next = node.next
                    self.count -= 1
                    self.size -= 1
                    return #d4ful
                else:
                    self.head = node.next
                    self.count -= 1
                    self.size -= 1
                    return #d4ful
            p_node = node
            node = node.next
        raise ValueError

class QuestionableList(object):
    '''
    I'm not sure this was neccesary, but hey, I'm the only one who's done it so far
    '''
    def __init__(self, init_list = None):
        self.count = 0
        self.head = None
        self.tail = None

        if init_list == None:
            init_list = []

        for i in init_list:
            self.append(i)

    def append(self, item):
        new_node = Node()
        step_node = Node(item)

        new_node.data = step_node
        self.count += 1
        if self.tail is not None:
            step_node.next = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        '''
        Always O(1), it's just plopped in front
        '''
        new_node = Node(next=self.head)
        step_node = Node(item)
        new_node.data = step_node
        self.head = new_node 
        self.count += 1
        if self.tail is not None:
            pass
        else:
            self.tail = new_node

    def items(self, process=lambda data: data):
        '''
        Always O(n), c'mon, what'd you expect? 

        pass a lambda process for fun & profit
        '''
        retlist = []
        node = self.head
        while node is not None:
            retlist.append(process(node.data.data))
            node = node.next
        return retlist

    def backwards_items(self, process=lambda data: data):
        '''
        Always O(n), c'mon, what'd you expect? 

        pass a lambda process for fun & profit
        '''
        retlist = []
        node = self.tail
        while node is not None:
            retlist.append(process(node.data.data))
            node = node.data.next
        return retlist

    def delete(self, item=None, quality=None):
        '''
        O(n) average/worst case, O(1) best case if the item is contained
        in the first node.
        '''
        p_node = None
        node = self.head
        while node != None:
            if quality is not None:
                if quality(node.data.data):
                    if node == self.tail:
                        self.tail = p_node
                    if node != self.head:
                        p_node.next = node.next
                        self.count -= 1
                        return #d4ful
                    else:
                        self.head = node.next
                        self.count -= 1
                        return #d4ful

            elif node.data.data == item or item == None:
                if node == self.tail:
                    self.tail = p_node
                if node != self.head:
                    p_node.next = node.next
                    self.count -= 1
                    return #d4ful
                else:
                    self.head = node.next
                    self.count -= 1
                    return #d4ful
            p_node = node
            node = node.next
        raise ValueError

    def backwards_delete(self, item=None, quality=None):
        '''
        O(n) average/worst case, O(1) best case if the item is contained
        in the first node.
        '''

        #fix next.previous
        p_node = None
        node = self.tail
        while node != None:
            if quality is not None:
                if quality(node.data.data):
                    if node == self.tail:
                        self.tail = p_node
                    if node != self.head:
                        p_node.data.next = node.data.next
                        self.count -= 1
                        return #d4ful
                    else:
                        self.head = node.data.next
                        self.count -= 1
                        return #d4ful

            elif node.data.data == item:
                if node == self.tail:
                    self.tail = p_node
                if node != self.head:
                    p_node.data.next = node.data.next
                    self.count -= 1
                    return #d4ful
                else:
                    self.head = node.data.next
                    self.count -= 1
                    return #d4ful
            p_node = node
            node = node.data.next
        raise ValueError


    def find(self, quality):
        '''
        '''
        node = self.head
        while node != None:
            if quality(node.data.data):
                return node.data.data
            node = node.next
        #return False

    def length(self):
        return self.length