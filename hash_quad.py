import math


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, table_size):  # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is bigger than table_size '''
        if self.is_prime(table_size):
            table_size = table_size
        else:
            table_size = self.next_prime(table_size)
        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.entries = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        entry = Node(key, value)
        index = self.horner_hash(key) % self.table_size
        start = index

        i = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == entry.key:
                self.hash_table[index].value = entry.value
                return
            i += 1
            index = start + (i ** 2)
            while index > self.table_size - 1:
                index = index - self.table_size
        self.hash_table[index] = entry
        self.entries += 1

        if self.get_load_factor() > 0.5:
            self.rehash()

    def rehash(self):
        temp = self.hash_table
        self.table_size = self.next_prime(self.table_size * 2)
        self.hash_table = [None] * self.table_size
        self.entries = 0
        for entry in temp:
            if entry is not None:
                self.insert(entry.key, entry.value)

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification. '''
        n = min(8, len(key))
        hash_value = 0
        for i in range(n):
            hash_value += (ord(key[i]) * 31 ** (n - 1 - i))
        return hash_value

    def next_prime(self, n):
        ''' Find the next prime number that is > n.'''
        if n <= 1:
            return 2

        prime = n
        found = False

        while not found:
            prime = prime + 1

            if self.is_prime(prime):
                found = True

        return prime

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        index = self.horner_hash(key) % self.table_size
        start = index
        i = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return True
            else:
                i += 1
                index = start + (i ** 2)
                while index > self.table_size - 1:
                    index = index - self.table_size
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. '''
        index = self.horner_hash(key) % self.table_size
        start = index
        i = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return index
            else:
                i += 1
                index = start + (i ** 2)
                while index > self.table_size - 1:
                    index = index - self.table_size
        return None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for entry in self.hash_table:
            if entry is not None:
                keys.append(entry.key)
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.horner_hash(key) % self.table_size
        start = index
        i = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value
            else:
                i += 1
                index = start + (i ** 2)
                while index > self.table_size - 1:
                    index = index - self.table_size
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.entries

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.entries / self.table_size
