"""!
@file Math_lib_tests.py
@brief Tests for Math_lib.py
@author Matej Hložek, xhloze02, PyJaMa's
@date March 2021
"""


import unittest
from Math_lib import *


def test_ok(test_name: str):
    """!@brief Test control"""
    print("Test {}: ok".format(test_name))


class TestAddition(unittest.TestCase):
    """!@brief Tests for addition function"""
    def testInteger(self):
        """!@brief Tests for addition of integers"""
        self.assertEqual(add(0, 0), 0)

        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(5, 8), 13)
        self.assertEqual(add(-6, 9), 3)
        self.assertEqual(add(-12, -8), -20)

        self.assertNotEqual(add(1, 1), 3)
        self.assertNotEqual(add(7, 6), 15)
        self.assertNotEqual(add(-3, 8), 50)
        self.assertNotEqual(add(-9, -8), -25)

        test_ok("Integer addition")

    def testFloat(self):
        """!@brief Tests for addition of floats"""
        self.assertAlmostEqual(add(0.0, 0.0), 0.0)

        self.assertAlmostEqual(add(1.0, 1.0), 2.0)
        self.assertAlmostEqual(add(2.9, 5.3), 8.2)
        self.assertAlmostEqual(add(-5.9, 8.3), 2.4)
        self.assertAlmostEqual(add(-3.8, -8.3), -12.1)

        self.assertNotAlmostEqual(add(1.0, 1.0), 5.3)
        self.assertNotAlmostEqual(add(6.9, 4.2), 0.5)
        self.assertNotAlmostEqual(add(-25.5, 14.7), 50.9)
        self.assertNotAlmostEqual(add(-4.4, -27.2), 7.3)

        test_ok("Float addition")


class TestSubtraction(unittest.TestCase):
    """!@brief Tests for subtraction function"""
    def testInteger(self):
        """!@brief Tests for subtraction of integers"""
        self.assertEqual(sub(0, 0), 0)

        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-9, 6), -15)
        self.assertEqual(sub(-5, -14), 9)

        self.assertNotEqual(sub(1, 1), 5)
        self.assertNotEqual(sub(9, 2), 12)
        self.assertNotEqual(sub(-4, 12), 17)
        self.assertNotEqual(sub(-8, -7), 4)

        test_ok("Integer subtraction")

    def testFloat(self):
        """!@brief Tests for subtraction of floats"""
        self.assertAlmostEqual(sub(0.0, 0.0), 0.0)

        self.assertAlmostEqual(sub(1.1, 1.1), 0.0)
        self.assertAlmostEqual(sub(8.9, 0.9), 8.0)
        self.assertAlmostEqual(sub(-7.9, 4.5), -12.4)
        self.assertAlmostEqual(sub(-8.3, -14.7), 6.4)

        self.assertNotAlmostEqual(sub(1.1, 1.1), 8.2)
        self.assertNotAlmostEqual(sub(4.8, 14.5), -8.2)
        self.assertNotAlmostEqual(sub(-18.5, 2.8), 12.1)
        self.assertNotAlmostEqual(sub(-4.9, -9.6), -1.5)

        test_ok("Float subtraction")


class TestMultiplication(unittest.TestCase):
    """!@brief Tests for multiplication function"""
    def testMultByZero(self):
        """!@brief Tests for multiplication by zero"""
        self.assertEqual(mult(1457, 0), 0)
        self.assertAlmostEqual(mult(24.579, 0.0), 0.0)

        test_ok("Multiply by zero")

    def testMultByOne(self):
        """!@brief Tests for multiplication by one"""
        self.assertEqual(mult(5, 1), 5)
        self.assertEqual(mult(6.4, 1), 6.4)

        test_ok("Multiply by one")

    def testInteger(self):
        """!@brief Tests for multiplication by integer"""
        self.assertEqual(mult(5, 5), 25)
        self.assertEqual(mult(8, 7), 56)
        self.assertEqual(mult(-4, 9), -36)
        self.assertEqual(mult(-8, -10), 80)

        self.assertNotEqual(mult(1, 1), -10)
        self.assertNotEqual(mult(5, 4), 50)
        self.assertNotEqual(mult(-9, 12), 16)
        self.assertNotEqual(mult(-7, -2), -14)

        test_ok("Integer multiplication")

    def testFloat(self):
        """!@brief Tests for multiplication by float"""
        self.assertAlmostEqual(mult(8.4, 1.5), 12.6, places=2)
        self.assertAlmostEqual(mult(4.7, 8.2), 38.54, places=2)
        self.assertAlmostEqual(mult(-5.7, 0.2), -1.14, places=2)
        self.assertAlmostEqual(mult(-9.2, -4.5), 41.4, places=2)

        self.assertNotAlmostEqual(mult(0.1, 10.0), 5, places=2)
        self.assertNotAlmostEqual(mult(5.9, 6.7), 0.2, places=2)
        self.assertNotAlmostEqual(mult(-7.4, 5.9), 20.4, places=2)
        self.assertNotAlmostEqual(mult(-3.4, -5.3), -15.5, places=2)

        test_ok("Float multiplication")


class TestDivision(unittest.TestCase):
    """!@brief Tests for division function"""
    def testDivByZero(self):
        """!@brief Tests for division by zero"""
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)
            div(7.3, 0)

        test_ok("Division by zero")

    def testDivByOne(self):
        """!@brief Tests for division by one"""
        self.assertAlmostEqual(div(1, 1), 1)
        self.assertAlmostEqual(div(5, 1), 5)

        test_ok("Division by one")

    def testDivBySameNum(self):
        """!@brief Tests for division by same number"""
        self.assertAlmostEqual(div(9.5, 9.5), 1.0)
        self.assertAlmostEqual(div(45.1, 45.1), 1.0)

        test_ok("Division by same number")

    def testFloat(self):
        """!@brief Tests for division by same float"""
        self.assertAlmostEqual(div(5, 2), 2.5)
        self.assertAlmostEqual(div(8, 4), 2.0)
        self.assertAlmostEqual(div(-24, 8), -3.0)
        self.assertAlmostEqual(div(-50, -5), 10.0)

        self.assertAlmostEqual(div(5.8, 2.2), 2.636363, places=4)
        self.assertAlmostEqual(div(5.2, 9.6), 0.541666, places=4)
        self.assertAlmostEqual(div(-28.6, 8), -3.575, places=4)
        self.assertAlmostEqual(div(-50.9, -4.3), 11.837209, places=4)

        test_ok("Basic division")


class TestPower(unittest.TestCase):
    """!@brief Tests for power function"""
    def testNotNaturalNumber(self):
        """!@brief Tests for exception with power of not a natural number"""
        with self.assertRaises(ValueError):
            pow(1, -5)
            pow(1, 5.5)

        test_ok("Power with natural number exponent")

    def testIntegerByInteger(self):
        """!@brief Tests for integer's power of integer"""
        self.assertEqual(pow(5, 3), 125)
        self.assertEqual(pow(-4, 3), -64)
        self.assertEqual(pow(12, 2), 144)
        self.assertEqual(pow(-3, 2), 9)

        test_ok("Power of integer with integer exponent")

    def testFloatByInteger(self):
        """!@brief Tests for float's power of integer"""
        self.assertAlmostEqual(pow(2.5, 3), 15.625, places=2)
        self.assertAlmostEqual(pow(-1.8, 5), -18.8956, places=2)
        self.assertAlmostEqual(pow(6.8, 2), 46.24, places=2)
        self.assertAlmostEqual(pow(-4.5, 4), 410.0625, places=2)

        test_ok("Power of float with integer exponent")


class TestRoot(unittest.TestCase):
    """!@brief Tests for root function"""
    def testNotNaturalNumber(self):
        """!@brief Tests for exception with root of not a natural number"""
        with self.assertRaises(ValueError):
            root(1, -5)
            root(1, 2.2)

        test_ok("Root with natural number exponent")

    def testNegativeNumber(self):
        """!@brief Tests for exception with root of a negative number"""
        with self.assertRaises(ValueError):
            root(-5, 2)
            root(-10, 4)

        test_ok("Root of negative number")

    def testInteger(self):
        """!@brief Tests for integer's root of integer"""
        self.assertAlmostEqual(root(10, 2), 3.1622, places=3)
        self.assertAlmostEqual(root(42, 2), 6.4807, places=3)
        self.assertAlmostEqual(root(-50, 3), -3.6840, places=3)
        self.assertAlmostEqual(root(-23, 3), -2.8438, places=3)
        self.assertAlmostEqual(root(4096, 4), 8)
        self.assertAlmostEqual(root(56, 3), 3.8258, places=3)

        test_ok("Integer root")

    def testFloat(self):
        """!@brief Tests for float's root of integer"""
        self.assertAlmostEqual(root(57.2, 2), 7.56306, places=2)
        self.assertAlmostEqual(root(152.7, 2), 12.3571, places=3)
        self.assertAlmostEqual(root(-48.12, 3), -3.6372, places=3)
        self.assertAlmostEqual(root(-999.65, 5), -3.9807, places=3)
        self.assertAlmostEqual(root(1562, 4), 6.2866, places=3)
        self.assertAlmostEqual(root(1285, 5), 4.1858, places=3)

        test_ok("Float root")


class TestFactorial(unittest.TestCase):
    """!@brief Tests for factorial function"""
    def testNotNaturalNumber(self):
        """!@brief Tests for exceptions with the factorial of not a natural number"""
        with self.assertRaises(ValueError):
            fact(-5)
            fact(4.1)

        test_ok("Factorial of negative number")

    def testFactOfOne(self):
        """!@brief Test for the factorial of one"""
        self.assertEqual(fact(1), 1)

        test_ok("Factorial of one")

    def testInteger(self):
        """!@brief Test for the factorial of an integer"""
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(7), 5040)

        test_ok("Basic factorial")


class TestSine(unittest.TestCase):
    """!@brief Tests for sine function"""
    def testInteger(self):
        """!@brief Tests for sine of an integer"""
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(180), 0)
        self.assertAlmostEqual(sin(270), -1)

        self.assertAlmostEqual(sin(15), 0.2588, places=3)
        self.assertAlmostEqual(sin(200), -0.342, places=3)
        self.assertAlmostEqual(sin(-5000), 0.6427, places=3)

        test_ok("Integer sine")

    def testFloat(self):
        """!@brief Tests for sine of a float"""
        self.assertAlmostEqual(sin(80.5), 0.9862, places=3)
        self.assertAlmostEqual(sin(126.1), 0.8079, places=3)
        self.assertAlmostEqual(sin(352.7), -0.127, places=3)

        test_ok("Float sine")


class TestCosine(unittest.TestCase):
    """!@brief Tests for cosine function"""
    def testInteger(self):
        """!@brief Tests for cosine function of an integer"""
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(180), -1)
        self.assertAlmostEqual(cos(270), 0)

        self.assertAlmostEqual(cos(35), 0.8191, places=3)
        self.assertAlmostEqual(cos(153), -0.891, places=3)
        self.assertAlmostEqual(cos(-301), 0.515, places=3)

        test_ok("Integer cosine")

    def testFloat(self):
        """!@brief Tests for cosine function of a float"""
        self.assertAlmostEqual(cos(111.52), -0.3668, places=3)
        self.assertAlmostEqual(cos(205.14), -0.9052, places=3)
        self.assertAlmostEqual(cos(-98.9), -0.1547, places=3)

        test_ok("Float cosine")


class TestTangent(unittest.TestCase):
    """!@brief Tests for tangent function"""
    def testNotDefined(self):
        """!@brief Tests for exceptions with the tangent of its undefined values"""
        with self.assertRaises(ValueError):
            tan(90)
            tan(270)

        test_ok("Not defined values of tangent")

    def testInteger(self):
        """!@brief Tests for tangent of an integer"""
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(180), 0)
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(135), -1)

        self.assertAlmostEqual(tan(99), -6.3137, places=3)
        self.assertAlmostEqual(tan(170), -0.1763, places=3)
        self.assertAlmostEqual(tan(-666), 1.3763, places=3)

        test_ok("Integer tangent")

    def testFloat(self):
        """!@brief Tests for tangent of a float"""
        self.assertAlmostEqual(tan(105.2), -3.6806, places=3)
        self.assertAlmostEqual(tan(209.7), 0.5703, places=3)
        self.assertAlmostEqual(tan(25.6), 0.4791, places=3)

        test_ok("Float tangent")


class TestCotangent(unittest.TestCase):
    """!@brief Tests for cotangent function"""
    def testNotDefined(self):
        """!@brief Tests for exceptions with the cotangent of its undefined values"""
        with self.assertRaises(ValueError):
            cotg(0)
            cotg(180)

        test_ok("Not defined values of cotangent")

    def testInteger(self):
        """!@brief Tests for cotangent of an integer"""
        self.assertAlmostEqual(cotg(45), 1)
        self.assertAlmostEqual(cotg(135), -1)
        self.assertAlmostEqual(cotg(225), 1)
        self.assertAlmostEqual(cotg(315), -1)

        self.assertAlmostEqual(cotg(221), 1.1503, places=3)
        self.assertAlmostEqual(cotg(95), -0.0874, places=3)
        self.assertAlmostEqual(cotg(-72), -0.3249, places=3)

        test_ok("Integer cotangent")

    def testFloat(self):
        """!@brief Tests for cotangent of a float"""
        self.assertAlmostEqual(cotg(320.6), -1.2174, places=3)
        self.assertAlmostEqual(cotg(182.8), 20.4464, places=3)
        self.assertAlmostEqual(cotg(82.5), 0.1316, places=3)

        test_ok("Float cotangent")


class TestConstants(unittest.TestCase):
    """!@brief Tests for constants in functions"""
    def testPi(self):
        """!@brief Tests for the constant "pi" """
        self.assertAlmostEqual(pi, 3.14159265359, places=6)

        self.assertAlmostEqual(add(pi, 10), 13.14159265359, places=4)
        self.assertAlmostEqual(sub(pi, 3), 0.14159265359, places=4)

        self.assertAlmostEqual(mult(pi, 2), 6.283185, places=4)
        self.assertAlmostEqual(div(150, pi), 47.746482, places=4)

        self.assertAlmostEqual(pow(pi, 2), 9.869604, places=4)
        self.assertAlmostEqual(root(pi, 2), 1.772453, places=4)

        with self.assertRaises(ValueError):
            pow(5, pi)
            root(5, pi)
            fact(pi)

        test_ok("Constant pi")

    def testE(self):
        """!@brief Tests for the constant "e" """
        self.assertAlmostEqual(e, 2.71828182846, places=6)

        self.assertAlmostEqual(add(e, 10), 12.71828182846, places=4)
        self.assertAlmostEqual(sub(e, 2), 0.71828182846, places=4)

        self.assertAlmostEqual(mult(e, 2), 5.436563, places=4)
        self.assertAlmostEqual(div(150, e), 55.181916, places=4)

        self.assertAlmostEqual(pow(e, 2), 7.389056, places=3)
        self.assertAlmostEqual(root(e, 2), 1.648721, places=4)

        with self.assertRaises(ValueError):
            pow(5, e)
            root(5, e)
            fact(e)

        test_ok("Constant e")


if __name__ == '__main__':
    unittest.main()
    print("All tests passed")
