import unittest
import io
import sys
from unittest.mock import patch

class Test02_mathematics_numbers_whoami_getname(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 **** GIVEN: import mathematics.numbers.whoami as whoami *** FUNCTION CALL: whoami.getname() *** EXPECT: 'mathematics.numbers.whoami' ***
        """
        import mathematics.numbers.whoami as whoami
        self.assertEqual('mathematics.numbers.whoami', whoami.getname())
        print()

class Test03_mathematics_numbers_series_sum(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 **** GIVEN: import mathematics.numbers.series as series *** FUNCTION CALL: series.sum(list = [1, 2, 3, 4, 5]) *** EXPECT: 15 ***
        """
        import mathematics.numbers.series as series
        self.assertEqual(15, series.sum(list = [1, 2, 3, 4, 5]))
        print()

class Test04_mathematics_numbers_series_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 **** GIVEN: import mathematics.numbers.series as series *** FUNCTION CALL: series.average(list = [1, 2, 3, 4, 5]) *** EXPECT: 3.0 ***
        """
        import mathematics.numbers.series as series
        self.assertEqual(3.0, series.average(list = [1, 2, 3, 4, 5]))
        print()

class Test05_mathematics_numbers_simple_addition(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 **** GIVEN: import mathematics.numbers.simple as simple *** FUNCTION CALL: simple.addition(left = 6, right = 7) *** EXPECT: 13 ***
        """
        import mathematics.numbers.simple as simple
        self.assertEqual(13, simple.addition(left = 6, right = 7))
        print()

class Test06_mathematics_numbers_simple_subtraction(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 **** GIVEN: import mathematics.numbers.simple as simple *** FUNCTION CALL: simple.subtraction(left = 6, right = 7) *** EXPECT: -1 ***
        """
        import mathematics.numbers.simple as simple
        self.assertEqual(-1, simple.subtraction(left = 6, right = 7))
        print()

class Test07_mathematics_numbers_simple_multiplication(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 **** GIVEN: import mathematics.numbers.simple as simple *** FUNCTION CALL: simple.multiplication(left = 6, right = 7) *** EXPECT: 42 ***
        """
        import mathematics.numbers.simple as simple
        self.assertEqual(42, simple.multiplication(left = 6, right = 7))
        print()

class Test08_mathematics_numbers_simple_division(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 **** GIVEN: import mathematics.numbers.simple as simple *** FUNCTION CALL: simple.division(left = 10, right = 4) *** EXPECT: 2.5 ***
        """
        import mathematics.numbers.simple as simple
        self.assertEqual(2.5, simple.division(left = 10, right = 4))
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
