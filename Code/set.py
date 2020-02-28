from hash_browns import Hashbrowns

class Set:

    def __init__(self):
        self.table = Hashbrowns()
        self.size = 0

    def contains(self, item):
        """
        O(l)
        """
        if self.table.contains(item):
            return True
        return False

    def add(self, item):
        """
        O(1)
        """
        if self.contains(item):
            raise ValueError
        self.table.set(item, True)
        self.size += 1

    def set_add(self, item):
        """
        O(1)
        """
        if self.contains(item):
            raise ValueError
        self.table.set(item, True)
        self.size += 1

    def remove(self, item):
        """
        O(l)
        """
        if self.contains(item):
            self.table.delete(item)
            self.size -= 1
        else:
            raise ValueError

    def length(self):
        """
        O(1)
        """
        return self.size

    def intersect(self, set_in):
        """
        O(n1) where n1 < n2 
        """
        retset = Set()
        for item in self.table.keys():
            if item in set_in.table.keys():
                retset.add(item)
        return retset

    def union(self, set_in):
        """
        O(n1 + n2)
        """
        retset = Set()
        for item in self.table.values():
            retset.add(item)

        for item in set_in.table.values:
            retset.set_add(item)

    def un_intersect(self, set_in):
        """
        O(n1) where n1 < n2 
        """
        s1 = self.intersect(set_in)
        s2 = self.union(set_in)
        for item in s1.table.values():
            s2.remove(item)
        return s2

    def is_subset(self, set_in):
        """
        O(n1) where n1 < n2 
        """
        for item in set_in.table.values():
            if not self.contains(item):
                return False
        return True
        
