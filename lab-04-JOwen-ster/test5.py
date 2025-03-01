import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test05_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: delete_contact(c, id = 7145551111) *** EXPECT: c = {5625553333: ['Bill', 'Gates']} ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        delete_contact(c, id = 7145551111)
        self.assertEqual(c, {5625553333: ['Bill', 'Gates']})
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
