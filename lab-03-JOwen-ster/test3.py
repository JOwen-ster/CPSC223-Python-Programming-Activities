import unittest
import io
import sys
from unittest.mock import patch

from contacts import *


class Test03_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** Calling the 'modify_contact' method passing a positional argument equal to [['Richard','Stallman'], a keyword argument first_name equal to 'Steve', a keyword argument last_name equal to 'Jobs', and a keyword argument index equal to '5' should result in a contact list [['Richard','Stallman']] and a return value of False ***
        """
        contacts = [["Richard","Stallman"]]
        x = modify_contact(contacts, index = 5, first_name = "Steve", last_name = "Jobs")
        self.assertEqual(contacts, [['Richard', 'Stallman']])
        self.assertEqual(x, False)
        print()



if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
