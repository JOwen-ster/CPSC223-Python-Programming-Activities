import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test03_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: modify_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman') *** EXPECT: c = {7145551111: ['Richard', 'Stallman'], 5625553333: ['Bill', 'Gates']} ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        modify_contact(c, id = 7145551111, first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(c, {7145551111: ['Richard', 'Stallman'], 5625553333: ['Bill', 'Gates']})
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
