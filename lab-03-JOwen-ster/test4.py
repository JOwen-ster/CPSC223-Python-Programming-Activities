import unittest
import io
import sys
from unittest.mock import patch

from contacts import *



class Test04_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** Calling the 'delete_contact' method passing a positional argument equal to [['Richard','Stallman'],['Bill','Gates'],['Steve','Jobs']], and a keyword argument index equal to '1' should result in a contact list [['Richard','Stallman'],['Steve','Jobs']] ***
        """
        contacts = [["Richard","Stallman"],["Bill","Gates"],["Steve","Jobs"]]
        delete_contact(contacts, index = 1)
        self.assertEqual(contacts, [['Richard', 'Stallman'], ['Steve', 'Jobs']])
        print()



if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
