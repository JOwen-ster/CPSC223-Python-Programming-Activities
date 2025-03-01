import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test02_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = add_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: r = 'error' ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = add_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
