# test_.py
from main import two_sum, length_of_last_word, search_insert
import unittest

class TestFunctions(unittest.TestCase):
    # Test cases for two_sum function
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1], "Test Case 1 Failed")
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2], "Test Case 2 Failed")
        self.assertEqual(two_sum([3, 3], 6), [0, 1], "Test Case 3 Failed")

    # Test cases for length_of_last_word function
    def test_length_of_last_word(self):
        self.assertEqual(length_of_last_word("Hello World"), 5, "Test Case 1 Failed")
        self.assertEqual(length_of_last_word("   fly me   to   the moon  "), 4, "Test Case 2 Failed")
        self.assertEqual(length_of_last_word("luffy is still joyboy"), 6, "Test Case 3 Failed")

    # Test cases for search_insert function
    def test_search_insert(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 5), 2, "Test Case 1 Failed")
        self.assertEqual(search_insert([1, 3, 5, 6], 2), 1, "Test Case 2 Failed")
        self.assertEqual(search_insert([1, 3, 5, 6], 7), 4, "Test Case 3 Failed")

if __name__ == '__main__':
    unittest.main()
