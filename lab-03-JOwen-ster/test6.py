import unittest
import io
import sys
from unittest.mock import patch

from contacts import *


class Test06_SortContacts(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** Calling the 'sort_contacts' method passing a positional argument equal to [['Richard','Stallman'],['Bill','Gates'],['Steve','Jobs']], and a keyword argument column equal to '0' should result in a contact list [['Bill','Gates'], ['Richard', 'Stallman'], ['Steve', 'Jobs']] ***
        """
        contacts = [["Richard","Stallman"],["Bill","Gates"],["Steve","Jobs"]]
        sort_contacts(contacts, column = 0)
        self.assertEqual(contacts, [['Bill','Gates'], ['Richard', 'Stallman'], ['Steve', 'Jobs']])
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
