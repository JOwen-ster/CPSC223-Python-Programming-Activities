import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test08_FindContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 *** GIVEN: c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = find_contact(c, find = 'jobs') *** EXPECT: r = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs']} ***
        """
        c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = find_contact(c, find = 'jobs')
        self.assertEqual(r, {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs']})
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
