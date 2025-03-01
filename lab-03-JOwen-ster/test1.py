import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test01_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** Calling the 'add_contact' method passing a positional argument equal to [['Richard','Stallman']], a keyword argument first_name equal to 'Steve', and a keyword argument last_name equal to 'Jobs' should result in a contact list [['Richard','Stallman'],['Steve','Jobs']] ***
        """
        contacts = [["Richard","Stallman"]]
        add_contact(contacts, first_name = "Steve", last_name = "Jobs")
        self.assertEqual(contacts, [['Richard', 'Stallman'], ['Steve', 'Jobs']])
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
