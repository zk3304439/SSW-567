"""Author:Yiyang Shi
   Program content:HW01: Classify Triangle
   unittest: Write some tests to check the Triangle.
"""

import unittest

from HW01_Yiyang_Shi import classifytriangle


class TriangleTest(unittest.TestCase):
    """Test Triangle"""
    def test_invalid(self):
        """Test invalid triangle"""
        self.assertEqual(classifytriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifytriangle(1, 2, 5), 'NotATriangle', '1,2,5 is not a triangle')

    def test_triangle(self):
        """Test triangle"""
        self.assertEqual(classifytriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')
        self.assertEqual(classifytriangle(10, 10, 10), 'Equilateral', '10,10,10 Should be Equilateral')
        self.assertEqual(classifytriangle(15, 16, 30), 'Scalene', '15,16,30 Should be Scalene')
        self.assertEqual(classifytriangle(1, 2, 2), 'Isosceles', '1,2,2 should be Isosceles')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)