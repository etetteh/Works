"""Hash tables are a type of data structure in, which the address or the index value of the data element is generated from a hash function.
   Hash function converts a key into an array index.
   There are several hash functions, but a better hash function is to use the ASCII value for each letter in a key.
   The time complexity for adding, getting, and deleting functions or items is O(1)."""

class HashTable(object):
    def __init__(self):
        # constructs empty fixed array of size 10000 
        self.table = [None] * 10000
    
    # calculate hash value based on a particular hash function
    def get_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value
    
    # Add calculated hash value to list
    def add_value(self, string):
        hv = self.get_hash_value(string)
        
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]
                
    def lookup(self, string):
        hv = self.get_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1
    

# Setup
hash_table = HashTable()

# Test calculate_hash_value
print(hash_table.get_hash_value('ENOCHTETTEH'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('ENOCHTETTEH'))

# Test store
hash_table.add_value('ENOCHTETTEH')
print(hash_table.lookup('ENOCHTETTEH'))

# Test store edge case
hash_table.add_value('ENOCHTETT')
print(hash_table.lookup('ENOCHTETT'))
