import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test01_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: add_contact(c, id = 7145551212, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates'], 7145551212: ['Richard', 'Stallman']} ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        add_contact(c, id = 7145551212, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(c, {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates'], 7145551212: ['Richard', 'Stallman']})
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
