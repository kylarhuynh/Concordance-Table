from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table is 191."""
        self.stop_table = HashTable(191)
        try:
            with open(filename) as stops:
                for line in stops:
                    if line[-1:] == "\n":
                        self.stop_table.insert(line[:-1])
                    else:
                        self.stop_table.insert(line)
        except FileNotFoundError:
            raise FileNotFoundError
        stops.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Does not include duplicate line numbers (word appearing on same line more than once.)
        Starting size of hash table is 191."""
        
        self.concordance_table = HashTable(191)
        try:
            with open(filename) as text:
                i = 1
                for line in text:
                    line = line.lower()
                    line = line.replace("'", "")
                    for c in string.punctuation:
                        line = line.replace(c, " ")
                    line_list = line.split()
                    set_list = set(line_list)
                    for c in set_list:
                        if c.isalpha():
                            if self.stop_table.in_table(c):
                                continue
                            if self.concordance_table.in_table(c):
                                self.concordance_table.insert(c, self.concordance_table.get_value(c) + " " + str(i))
                            else:
                                self.concordance_table.insert(c, str(i))
                    i += 1
        except FileNotFoundError:
            raise FileNotFoundError
        text.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)"""
        result = self.concordance_table.get_all_keys()
        result.sort()
        output = open(filename, 'w')
        if not result:
            output.close()
            return
        output.write(result[0] + ": " + self.concordance_table.get_value(result[0]))
        for s in result[1:]:
            output.write("\n")
            output.write(s + ": " + self.concordance_table.get_value(s))
        output.close()
