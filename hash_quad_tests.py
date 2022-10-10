import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.horner_hash("cat"), 98262)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.in_table("dog"), False)
        self.assertEqual(ht.in_table("cats"), False)
        self.assertEqual(ht.next_prime(7), 11)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)
        self.assertEqual(ht.get_index("dog"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)
        self.assertEqual(ht.in_table("cat"), False)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01i(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 'a')
        self.assertEqual(ht.get_value("cat"), 'a')
        self.assertEqual(ht.get_all_keys(), ["cat"])


    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        self.assertEqual(ht.get_value("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_load_factor(), 3/7)
        self.assertEqual(ht.get_index("o"), 3)
        self.assertEqual(ht.get_value("o"), 0)
        ht.insert("v", 12) # Causes rehash
        self.assertEqual(ht.get_table_size(), 17)
        self.assertEqual(ht.get_load_factor(), 4 / 17)
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_value("h"), 0)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_value("o"), 0)
        self.assertEqual(ht.get_index("v"), 16)
        self.assertEqual(ht.get_value("v"), 12)
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_all_keys(), ["h", 'o', 'a', 'v'])

    def tests_prime(self):
        ht = HashTable(1)
        self.assertEqual(ht.is_prime(1), False)
        self.assertEqual(ht.is_prime(2), True)
        self.assertEqual(ht.is_prime(3), True)
        self.assertEqual(ht.is_prime(9), False)
        self.assertEqual(ht.next_prime(1), 2)

    def test_prime(self):
        ht = HashTable(1)
        self.assertEqual(ht.is_prime(77), False)

    def test_04(self):
        ht = HashTable(7)
        ht.insert("catapult", 5)
        self.assertEqual(ht.in_table("catapult"), True)
        self.assertEqual(ht.in_table("catapulted"), False)
        self.assertEqual(ht.horner_hash("catapult"), 2813250669592)
        self.assertEqual(ht.horner_hash("catapulted"), 2813250669592)


if __name__ == '__main__':
   unittest.main()
