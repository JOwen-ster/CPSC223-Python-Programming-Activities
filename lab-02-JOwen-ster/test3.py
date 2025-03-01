import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

class Test03_ModifyContact(unittest.TestCase):
    @patch("builtins.input", side_effect=[3])
    def test_list_int(self, mock_input):
        """
        *** Test03 *** Calling the 'modify_contact' method passing a contact list [['Richard','Stallman'],['Steve','Jobs']] and modifing the contact at index 3 shoud return 'Invalid index number.' ***
        """
        contacts = [["Richard","Stallman"],["Bill","Gates"]]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        result = modify_contact(contacts)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().replace("\n",""), "Invalid index number.")
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
