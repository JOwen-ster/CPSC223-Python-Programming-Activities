import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test01_AddContact(unittest.TestCase):
    @patch("builtins.input", side_effect=["Steve","Jobs"])
    def test_list_int(self, mock_input):
        """
        *** Test01 *** Calling the 'add_contact' method passing a contact list [['Richard','Stallman']] and adding the contact ['Steve','Jobs'] should return [['Richard','Stallman'],['Steve','Jobs']] ***
        """
        contacts = [["Richard","Stallman"]]
        result = add_contact(contacts)
        self.assertEqual(result, [['Richard', 'Stallman'], ['Steve', 'Jobs']])

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
