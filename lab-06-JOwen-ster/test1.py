import unittest
import main
import calculator
import io
import sys

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator.add(5.5, 3.0)
        self.assertEqual(result, 8.5)

    def test_subtraction(self):
        result = calculator.subtract(7.0, 3.5)
        self.assertEqual(result, 3.5)

    def test_multiplication(self):
        result = calculator.multiply(4.0, 2.5)
        self.assertEqual(result, 10.0)

    def test_division(self):
        result = calculator.divide(10.0, 2.0)
        self.assertEqual(result, 5.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5.0, 0.0)

# class TestMainProgram(unittest.TestCase):

#     def test_get_float_input_valid(self):
#         sys.stdin = io.StringIO('3.14\n')
#         result = main.get_float_input("Enter a number: ")
#         self.assertEqual(result, 3.14)

#     def test_get_float_input_invalid(self):
#         sys.stdin = io.StringIO('abc\n5.0\n')
#         result = main.get_float_input("Enter a number: ")
#         self.assertEqual(result, 5.0)

#     def test_main_program(self):
#         sys.stdin = io.StringIO('5.5\n3.0\ntest_results.json\n')
#         main.main()

if __name__ == '__main__':
    unittest.main()
