import unittest
import io
import sys
from unittest.mock import patch

class Test14_mathematics_init(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test14 **** GIVEN: import mathematics.__init__ as init *** FUNCTION CALL: init.__all__ *** EXPECT: ['whoami'] ***
        """
        import mathematics.__init__ as init
        self.assertEqual(['whoami'], init.__all__)
        print()

class Test15_mathematics_numbers_init(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test15 **** GIVEN: import mathematics.numbers.__init__ as init *** FUNCTION CALL: init.__all__ *** EXPECT: ['whoami', 'series'] ***
        """
        import mathematics.numbers.__init__ as init
        self.assertEqual(['whoami', 'series'], init.__all__)
        print()

class Test16_mathematics_geometry_init(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test16 **** GIVEN: import mathematics.geometry.__init__ as init *** FUNCTION CALL: init.__all__ *** EXPECT: ['whoami', 'circle', 'cube'] ***
        """
        import mathematics.geometry.__init__ as init
        self.assertEqual(['whoami', 'circle', 'cube'], init.__all__)
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
