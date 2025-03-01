import unittest
import io
import sys
from unittest.mock import patch

class Test01_mathematics_whoami_getname(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 **** GIVEN: import mathematics.whoami as whoami *** FUNCTION CALL: whoami.getname() *** EXPECT: 'mathematics.whoami' ***
        """
        import mathematics.whoami as whoami
        self.assertEqual('mathematics.whoami', whoami.getname())
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
