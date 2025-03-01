import unittest
import io
import sys
from unittest.mock import patch

class Test09_mathematics_geometry_whoami_getname(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 **** GIVEN: import mathematics.geometry.whoami as whoami *** FUNCTION CALL: whoami.getname() *** EXPECT: 'mathematics.geometry.whoami' ***
        """
        import mathematics.geometry.whoami as whoami
        self.assertEqual('mathematics.geometry.whoami', whoami.getname())
        print()

class Test10_mathematics_geometry_rectangle_perimeter(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test10 **** GIVEN: import mathematics.geometry.rectangle as rectangle *** FUNCTION CALL: rectangle.perimeter(length = 3, width = 7) *** EXPECT: 20 ***
        """
        import mathematics.geometry.rectangle as rectangle
        self.assertEqual(20, rectangle.perimeter(length = 3, width = 7))
        print()

class Test11_mathematics_geometry_rectangle_area(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test11 **** GIVEN: import mathematics.geometry.rectangle as rectangle *** FUNCTION CALL: rectangle.area(length = 3, width = 7) *** EXPECT: 21 ***
        """
        import mathematics.geometry.rectangle as rectangle
        self.assertEqual(21, rectangle.area(length = 3, width = 7))
        print()

class Test12_mathematics_geometry_cube_surfacearea(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test12 **** GIVEN: import mathematics.geometry.cube as cube *** FUNCTION CALL: cube.surface_area(side=5) *** EXPECT: 150 ***
        """
        import mathematics.geometry.cube as cube
        self.assertEqual(150, cube.surface_area(side=5))
        print()

class Test13_mathematics_geometry_cube_volume(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test13 **** GIVEN: import mathematics.geometry.cube as cube *** FUNCTION CALL: cube.volume(side=5) *** EXPECT: 125 ***
        """
        import mathematics.geometry.cube as cube
        self.assertEqual(125, cube.volume(side=5))
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
