

class AltTable:

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [None] * init_size
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'
    
    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())
    
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        return self.size / len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: O(b) best O(n + b) average/worst"""
        # Collect all keys in each of the buckets
        all_keys = []
        for kvp in self.buckets:
            if kvp is not None and kvp is not False:
                all_keys.append(kvp[0])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time:  O(b) best O(n + b) average/worst"""
        # Collect all values in each of the buckets
        all_values = []
        for kvp in self.buckets:
            if kvp is not None and kvp is not False:
                all_values.append(kvp[1])
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: O(b) best O(n + b) average/worst"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for kvp in self.buckets:
            if kvp is not None and kvp is not False:
                all_items.append(kvp)
        return all_items

    def length(self): # 
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: O(1) best O(n + b) average/worst """
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for kvp in self.buckets:
            if kvp is not None and kvp is not False:
                item_count += 1
        return item_count

    def contains(self, key): 
        """Return True if this hash table contains the given key, or False.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._locate_index(key)
        if index == False:
            return False
        return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._locate_index(key)
        if index == False:
            raise KeyError
        if index[1] == False:
            raise KeyError
        return self.buckets[index[0]][1]

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        index = self._locate_index(key, set_index=True)
        if index == False:
            raise ValueError
        if index[1] == True:
            self.size -= 1

        self.buckets[index[0]] = (key, value)
        self.size += 1
        
        if self.load_factor() > 0.75:
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        
        index = self._locate_index(key)
        if index == False:
            raise KeyError('Key not found: {}'.format(key))
        if index[1] == False:
            raise KeyError
        self.buckets[index[0]] = False
        self.size -= 1

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(n) runtime
        Best and worst case space usage: O(n), O(n) memory usage based on the
        new bucket abount"""
        # If unspecified, choose new size dynamically based on current size
        self.size = 0
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        setlist = self.items()
        self.buckets = [None] * new_size
        for item in setlist:
            if item is not False:
                self.set(item[0], item[1])
        
    def _locate_index(self, key, set_index=False):
        index = self._bucket_index(key)
        offset = -1
        while offset < self.size:
            offset += 1
            if self.size == 0:
                ndx = 0
                kvp = self.buckets[0]
            else:
                ndx = (index + offset) % len(self.buckets)
                kvp = self.buckets[ndx]               
            if set_index and kvp == None:
                return (ndx, 'Spaghetti')
            if kvp is not None and kvp is not False:
                if kvp[0] == key:
                    return (ndx, True)
            if kvp is False:
                return (ndx, False)
            
        return False

if __name__ == "__main__":
    s = AltTable()
    s.set('I', 11)    
