import sys
import os
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../'
        )
    )
)

import unittest
from matrices.matrix import Matrix


class TestMatrix(unittest.TestCase):
    """ Tests the interaction between matrices """

    def setUp(self) -> None:
        """ Setting up of matrices to use in the following tests """
        self.m1 = Matrix(3, 3, [4,-7,2,3,-4,-1,8,-9,7], 1)
        self.m2 = Matrix(3, 3, [7,5,-9,6,3,-4,8,-9,-1], 1)
        self.m3 = Matrix(6, 4, [8.7,-9.3,1,0,42,15.4,-11,7,2.6,-17,4.8,-5.6,
                                64,81,5,78,-42,-4,-1,57,7,-78,8,91], 1)
        self.m4 = Matrix(6, 4, [-57.2,-7,44.1,18,63.9,44.7,-32.6,-94,0,-61.9,
                                81.7,-16.4,99,72.1,-84.6,-10,-41.7,28.6,-73.1,
                                88,5,14,0,0], 1)
        self.m5 = Matrix(5, 3, [4.8,63.1,-27,36.4,-78.9,-17.6,10,0,-293.7,
                                88.4,76,11,-9.8,-17,165])
        self.m6 = Matrix(3, 6, [-33,57.4,1,96,-104.3,0.8,76,12.2,-69,11,2,
                                -178,64,-22,7.7,104.9,45.6,-354])

    def test_sum(self) -> None:
        """ Test the sum between Matrix objects
        
        Enters with two operations with known answer to verify the calculated 
        sum 
        """
        tests = (
            (
                self.m1, self.m2, (
                                    3, 3, [
                                            [11, -2, -7], [9, -1, -5], 
                                            [16, -18, 6]
                                        ]
                                )
            ),
            (
                self.m3, self.m4, (
                                    6, 4, [
                                            [-48.5, -16.3, 45.1, 18], 
                                            [105.9, 60.1, -43.6, -87], 
                                            [2.6, -78.9, 86.5, -22], 
                                            [163, 153.1, -79.6, 68], 
                                            [-83.7, 24.6, -74.1, 145], 
                                            [12, -64, 8, 91]
                                        ]
                                )
            )
        )
        for op1, op2, expected in tests:
            rows, columns, result = expected
            with self.subTest(op1=op1, op2=op2, expected=expected):
                sum = op1 + op2
                self.assertEqual(sum.values, result)
                self.assertEqual(sum.rows, rows)
                self.assertEqual(sum.columns, columns)

    
    def test_sub(self) -> None:
        """ Test the subtraction between Matrix objects
        
        Enters with two operations with known answer to verify the calculated 
        subtraction 
        """
        tests = (
            (
                self.m1, self.m2, (
                                    3, 3, [
                                            [-3, -12, 11], [-3, -7, 3], 
                                            [0, 0, 8]
                                        ]
                                )
            ),
            (
                self.m3, self.m4, (
                                    6, 4, [
                                            [65.9, -2.3, -43.1, -18], 
                                            [-21.9, -29.3, 21.6, 101], 
                                            [2.6, 44.9, -76.9, 10.8], 
                                            [-35, 8.9, 89.6, 88], 
                                            [-0.3, -32.6, 72.1, -31], 
                                            [2, -92, 8, 91]
                                        ]
                                )
            )
        )
        for op1, op2, expected in tests:
            rows, columns, result = expected
            with self.subTest(op1=op1, op2=op2, expected=expected):
                sub = op1 - op2
                self.assertEqual(sub.values, result)
                self.assertEqual(sub.rows, rows)
                self.assertEqual(sub.columns, columns)
    
    
    def test_mul(self) -> None:
        """ Test the multiplication between Matrix objects 
        
        Enters with two operations with known answer to verify the calculated 
        multiplication
        """
        tests = (
            (
                self.m1, self.m2, (
                                    3, 3, [
                                            [2, -19, -10], [-11, 12, -10], 
                                            [58, -50, -43]
                                        ]
                                )
            ),
            (
                self.m5, self.m6, 
                (
                    5, 6, 
                    [
                        [2909.2,1639.34,-4557,-1677.4,-1605.64,-1669.96], 
                        [-8324,1513.98,5344.98,780.26,-4756.88,20303.72], 
                        [-19126.8,7035.4,-2251.49,-29849.13,-14435.72,
                        103977.8], 
                        [3562.8,5759.36,-5070.9,10476.3,-8566.52,-17351.28], 
                        [9591.4,-4399.92,2433.7,16180.7,8512.14,-55391.84]
                    ]
                )
            )
        )
        for op1, op2, expected in tests:
            rows, columns, result = expected
            with self.subTest(op1=op1, op2=op2, expected=expected):
                mul = op1 * op2
                self.assertEqual(mul.values, result)
                self.assertEqual(mul.rows, rows)
                self.assertEqual(mul.columns, columns)
    
    def test_invalid_matrix_order(self) -> None:
        """ Test the input of values in the creation of the array 

        Enter an invalid number of values and expect an IndexError
        """
        with self.assertRaises(IndexError):
            m = Matrix(4, 4, [1, 2])
        
    def test_invalid_sum_operation(self) -> None:
        """ Test an invalid sum between Matrix objects 

        Try the sum between matrices of different order and expect a 
        ValueError
        """
        with self.assertRaises(ValueError):
            r = self.m1 + self.m3

    def test_invalid_sub_operation(self) -> None:
        """ Test an invalid subtraction between Matrix objects 

        Try the subtraction between matrices of different order and expect a 
        ValueError
        """
        with self.assertRaises(ValueError):
            r = self.m1 - self.m3

    def test_invalid_mul_operation(self) -> None:
        """ Test an invalid multiplication between Matrix objects 

        Try the multiplication between matrices that don't follow the rule of
        columns equal to rows and expect a ValueError
        """
        with self.assertRaises(ValueError):
            r = self.m1 * self.m3


if __name__ == '__main__':
    unittest.main(verbosity=2)
