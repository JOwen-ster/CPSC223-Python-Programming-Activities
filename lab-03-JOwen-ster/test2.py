import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test02_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** Calling the 'modify_contact' method passing a positional argument equal to [['Richard','Stallman'],['Bill','Gates']], a keyword argument first_name equal to 'Steve', a keyword argument last_name equal to 'Jobs', and a keyword argument index equal to '1' should result in a contact list [['Richard','Stallman'],['Steve','Jobs']] ***
        """
        contacts = [["Richard","Stallman"],["Bill","Gates"]]
        modify_contact(contacts, index = 1, first_name = "Steve", last_name = "Jobs")
        self.assertEqual(contacts, [['Richard', 'Stallman'], ['Steve', 'Jobs']])
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
