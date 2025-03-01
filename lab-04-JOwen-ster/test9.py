import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test09_FindContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test09 *** GIVEN: c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = find_contact(c, find = '5625553333') *** EXPECT: r = {5625553333: ['Bill', 'Gates']} ***
        """
        c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = find_contact(c, find = '5625553333')
        self.assertEqual(r, {5625553333: ['Bill', 'Gates']})
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
