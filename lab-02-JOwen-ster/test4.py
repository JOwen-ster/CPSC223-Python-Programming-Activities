import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test04_DeleteContact(unittest.TestCase):
    @patch("builtins.input", side_effect=[1])
    def test_list_int(self, mock_input):
        """
        *** Test04 *** Calling the 'delete_contact' method passing a contact list [['Richard','Stallman'],['Bill','Gates'],['Steve','Jobs']] and deleting the contact at index 1 should return [['Richard','Stallman'],['Steve','Jobs']] ***
        """
        contacts = [["Richard","Stallman"],["Bill","Gates"],["Steve","Jobs"]]
        result = delete_contact(contacts)
        self.assertEqual(result, [['Richard', 'Stallman'], ['Steve', 'Jobs']])


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
