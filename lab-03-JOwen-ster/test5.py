import unittest
import io
import sys
from unittest.mock import patch

from contacts import *


class Test05_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** Calling the 'delete_contact' method passing a positional argument equal to [['Richard','Stallman'],['Steve','Jobs']], and a keyword argument index equal to '5' should result in a contact list [['Richard','Stallman'],['Steve','Jobs']] and a return value of False ***
        """
        contacts = [["Richard","Stallman"],["Steve","Jobs"]]
        x = delete_contact(contacts, index = 5)
        self.assertEqual(contacts, [['Richard', 'Stallman'], ['Steve', 'Jobs']])
        self.assertEqual(x, False)
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
