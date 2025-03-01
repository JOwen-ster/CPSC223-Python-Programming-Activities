import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test06_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** GIVEN: c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} *** FUNCTION CALL: r = delete_contact(c, id = 7145559999) *** EXPECT: r = 'error' ***
        """
        c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
        r = delete_contact(c, id = 7145559999)
        self.assertEqual(r, 'error')
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
