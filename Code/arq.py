

class CyclicQ(object):
    '''
    Queue. 

    read parameter is next scheduled for dequeue, write parameter is 
    most recently queued.
    '''
    def __init__(self, length):
        self.width = length
        self.length = 0
        self.array = [None] * length  

        self.read = 0
        self.write = -1

    def enqueue(self, item):
        '''
        adds an item to the end of the queue
        '''
        if self.length == self.width:
            raise ValueError

        self.write += 1
        self.array[self.write % self.width] = item
        self.length += 1
        
    def dequeue(self):
        '''
        Returns the oldest item in queue
        '''
        if self.length == 0:
            raise ValueError

        self.length -= 1
        reval = self.array[self.read % self.width]
        self.read += 1
        return reval

    def scrollback(self):
        '''
        Lowers the read/write pointers back down into reasonable
        ranges, for sanity's sake I suppose.
        '''
        if self.write <= 0:
            return
        offset = self.read % self.width

        self.write -= self.read - offset
        self.read = offset




class FixedQ(object):
    '''
    Fixed length/width queue. Pass list equal to queue length for
    previous queue values. oldest -> newest

    dequeues on enqueue, head is next to be dequeued.
    '''
    def __init__(self, length, starter_list=None):
        self.width = length
        self.head = 0
        if starter_list is None:
            self.array = [None] * length  
        else:
            if len(starter_list) != length:
                raise  ValueError
            else:
                self.array = starter_list

    def __str__(self):
        '''
        stotrorrjw
        '''
        return ' '.join(self.items())

    def ndqueue(self, item):
        '''
        enqueue and dequeue at the same time!
        '''
        self.head = self.head % self.width
        reval = self.array[self.head]
        self.array[self.head] = item
        self.head += 1   
        return reval    

    def items(self):
        retlist = []
        index = self.head
        while index != self.head + self.width:
            retlist.append(self.array[index%self.width])
            index += 1
        return retlist



def test_q():
        qu = CyclicQ(4)

        qu.enqueue(1)
        qu.enqueue(2)
        assert qu.dequeue() == 1
        qu.enqueue(3)
        assert qu.dequeue() == 2
        assert qu.dequeue() == 3
        