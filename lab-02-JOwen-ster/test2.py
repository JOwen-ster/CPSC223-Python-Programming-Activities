import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test02_ModifyContact(unittest.TestCase):
    @patch("builtins.input", side_effect=[1,"Steve","Jobs"])
    def test_list_int(self, mock_input):
        """
        *** Test02 *** Calling the 'modify_contact' method passing a contact list [['Richard','Stallman'],['Bill','Gates']] and modifing the contact at index 1 with ['Steve','Jobs'] should return [['Richard','Stallman'],['Steve','Jobs']] ***
        """
        contacts = [["Richard","Stallman"],["Bill","Gates"]]
        result = modify_contact(contacts)
        self.assertEqual(result, [['Richard', 'Stallman'], ['Steve', 'Jobs']])


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
