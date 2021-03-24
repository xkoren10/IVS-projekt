"""
@file: Math_lib_tests.py
@brief: Tests for Math_lib.py
@author: Matej Hložek, xhloze02, PyJaMa's
@date: March 2021
"""


import unittest
from Math_lib import *


"""@brief: Tests for addition function"""
class TestAddition(unittest.TestCase):
    def testInteger(self):
        self.assertEqual(add(0, 0), 0)

        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(5, 8), 12)
        self.assertEqual(add(-6, 9), 3)
        self.assertEqual(add(-12, -8), -20)

        self.assertNotEqual(add(1, 1), 3)
        self.assertNotEqual(add(7, 6), 15)
        self.assertNotEqual(add(-3, 8), 50)
        self.assertNotEqual(add(-9, -8), -25)

    def testFloat(self):
        self.assertAlmostEqual(add(0.0, 0.0), 0.0)

        self.assertAlmostEqual(add(1.0, 1.0), 2.0)
        self.assertAlmostEqual(add(2.9, 5.3), 8.2)
        self.assertAlmostEqual(add(-5.9, 8.3), 2.4)
        self.assertAlmostEqual(add(-3.8, -8.3), -12.1)

        self.assertNotAlmostEqual(add(1.0, 1.0), 5.3)
        self.assertNotAlmostEqual(add(6.9, 4.2), 0.5)
        self.assertNotAlmostEqual(add(-25.5, 14.7), 50.9)
        self.assertNotAlmostEqual(add(-4.4, -27.2), 7.3)


"""@brief: Tests for subtraction function"""
class TestSubtraction(unittest.TestCase):
    def testInteger(self):
        self.assertEqual(sub(0, 0), 0)

        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-9, 6), -12)
        self.assertEqual(sub(-5, -14), 9)

        self.assertNotEqual(sub(1, 1), 5)
        self.assertNotEqual(sub(9, 2), 12)
        self.assertNotEqual(sub(-4, 12), 17)
        self.assertNotEqual(sub(-8, -7), 4)

    def testFloat(self):
        self.assertAlmostEqual(sub(0.0, 0.0), 0.0)

        self.assertAlmostEqual(sub(1.1, 1.1), 0.0)
        self.assertAlmostEqual(sub(8.9, 0.9), 8.0)
        self.assertAlmostEqual(sub(-7.9, 4.5), -12.4)
        self.assertAlmostEqual(sub(-8.3, -14.7), 6.4)

        self.assertNotAlmostEqual(sub(1.1, 1.1), 8.2)
        self.assertNotAlmostEqual(sub(4.8, 14.5), -8.2)
        self.assertNotAlmostEqual(sub(-18.5, 2.8), 12.1)
        self.assertNotAlmostEqual(sub(-4.9, -9.6), -1.5)


"""@brief: Tests for multiplication function"""
class TestMultiplication(unittest.TestCase):
    def testMultByZero(self):
        self.assertEqual(mult(1457, 0), 0)
        self.assertAlmostEqual(mult(24.579, 0.0), 0.0)

    def testMultByOne(self):
        self.assertEqual(mult(5, 1), 5)
        self.assertEqual(mult(6.4, 1), 6.4)

    def testInteger(self):
        self.assertEqual(mult(5, 5), 25)
        self.assertEqual(mult(8, 7), 56)
        self.assertEqual(mult(-4, 9), -36)
        self.assertEqual(mult(-8, -10), 80)

        self.assertNotEqual(mult(1, 1), -10)
        self.assertNotEqual(mult(5, 4), 50)
        self.assertNotEqual(mult(-9, 12), 16)
        self.assertNotEqual(mult(-7, -2), -14)

    def testFloat(self):
        self.assertAlmostEqual(mult(8.4, 1.5), 12.6)
        self.assertAlmostEqual(mult(4.7, 8.2), 38.54)
        self.assertAlmostEqual(mult(-5.7, 0.2), -1.14)
        self.assertAlmostEqual(mult(-9.2, -4.5), 41.4)

        self.assertNotAlmostEqual(mult(0.1, 10.0), 5)
        self.assertNotAlmostEqual(mult(5.9, 6.7), 0.2)
        self.assertNotAlmostEqual(mult(-7.4, 5.9), 20.4)
        self.assertNotAlmostEqual(mult(-3.4, -5.3), -15.5)


"""@brief: Tests for division function"""
class TestDivision(unittest.TestCase):
    def testDivByZero(self):
        self.assertRaises(div(5, 0))
        self.assertRaises(div(5.0, 0))

    def testDivByOne(self):
        self.assertAlmostEqual(div(1, 1), 1)
        self.assertAlmostEqual(div(5, 1), 5)

    def testDivBySameNum(self):
        self.assertAlmostEqual(div(9.5, 9.5), 1.0)
        self.assertAlmostEqual(div(45.1, 45.1), 1.0)

    def testFloat(self):
        self.assertAlmostEqual(div(5, 2), 2.5)
        self.assertAlmostEqual(div(8, 4), 2.0)
        self.assertAlmostEqual(div(-24, 8), -3.0)
        self.assertAlmostEqual(div(-50, -5), 10.0)

        self.assertAlmostEqual(div(5.8, 2.2), 2.63)
        self.assertAlmostEqual(div(5.2, 9.6), 0.5416)
        self.assertAlmostEqual(div(-28.6, 8), -3.575)
        self.assertAlmostEqual(div(-50.9, -4.3), 11.8372)


"""@brief: Tests for power function"""
class TestPower(unittest.TestCase):
    def testNotNaturalNumber(self):
        self.assertRaises(pow(1, -5))
        self.assertRaises(pow(1, 5.5))

    def testIntegerByInteger(self):
        self.assertEqual(pow(5, 3), 125)
        self.assertEqual(pow(-4, 3), -64)
        self.assertEqual(pow(12, 2), 144)
        self.assertEqual(pow(-3, 2), 9)

    def testFloatByInteger(self):
        self.assertAlmostEqual(pow(2.5, 3), 15.625)
        self.assertAlmostEqual(pow(-1.8, 5), -18.8956)
        self.assertAlmostEqual(pow(6.8, 2), 46.24)
        self.assertAlmostEqual(pow(-4.5, 4), 410.0625)


"""@brief: Tests for root function"""
class TestRoot(unittest.TestCase):
    def testNotNaturalNumber(self):
        self.assertRaises(root(1, -5))
        self.assertRaises(root(1, 2.2))

    def testNegativeNumber(self):
        self.assertRaises(root(-5, 2))
        self.assertRaises(root(-10, 4))

    def testInteger(self):
        self.assertAlmostEqual(root(10, 2), 3.1622)
        self.assertAlmostEqual(root(42, 2), 6.4807)
        self.assertAlmostEqual(root(-50, 3), -3.6840)
        self.assertAlmostEqual(root(-23, 3), -2.8438)
        self.assertAlmostEqual(root(4096, 4), 8)
        self.assertAlmostEqual(root(56, 3), 3.8258)

    def testFloat(self):
        self.assertAlmostEqual(root(57.6, 2), 7.563)
        self.assertAlmostEqual(root(152.7, 2), 12.3571)
        self.assertAlmostEqual(root(-48.12, 3), -3.6372)
        self.assertAlmostEqual(root(-999.65, 5), -3.9807)
        self.assertAlmostEqual(root(1562, 4), 6.2866)
        self.assertAlmostEqual(root(1285, 5), 4.1858)


"""@brief: Tests for factorial function"""
class TestFactorial(unittest.TestCase):
    def testNotNaturalNumber(self):
        self.assertRaises(fact(-5))
        self.assertRaises(fact(4.1))

    def testFactOfOne(self):
        self.assertEqual(fact(1), 1)

    def testInteger(self):
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(7), 5040)


"""@brief: Tests for sine function"""
class TestSine(unittest.TestCase):
    def testInteger(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(180), 0)
        self.assertAlmostEqual(sin(270), -1)

        self.assertAlmostEqual(sin(15), 0.2588)
        self.assertAlmostEqual(sin(200), -0.342)
        self.assertAlmostEqual(sin(5000), -0.6427)

    def testFloat(self):
        self.assertAlmostEqual(sin(80.5), 0.9862)
        self.assertAlmostEqual(sin(126.1), 0.8079)
        self.assertAlmostEqual(sin(352.7), -0.127)


"""@brief: Tests for cosine function"""
class TestCosine(unittest.TestCase):
    def testInteger(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(180), -1)
        self.assertAlmostEqual(cos(270), 0)

        self.assertAlmostEqual(cos(35), 0.8191)
        self.assertAlmostEqual(cos(153), -0.891)
        self.assertAlmostEqual(cos(301), 0.515)

    def testFloat(self):
        self.assertAlmostEqual(cos(111.52), -0.3668)
        self.assertAlmostEqual(cos(205.14), -0.9052)
        self.assertAlmostEqual(cos(98.9), -0.1547)


"""@brief: Tests for tangent function"""
class TestTangent(unittest.TestCase):
    def testNotDefined(self):
        self.assertRaises(tan(90))
        self.assertRaises(tan(270))

    def testInteger(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(180), 0)
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(135), -1)

        self.assertAlmostEqual(tan(99), -6.3137)
        self.assertAlmostEqual(tan(170), -0.1763)
        self.assertAlmostEqual(tan(666), -1.3763)

    def testFloat(self):
        self.assertAlmostEqual(tan(105.2), -3.6806)
        self.assertAlmostEqual(tan(209.7), 0.5703)
        self.assertAlmostEqual(tan(25.6), 0.4791)


"""@brief: Tests for cotangent function"""
class TestTangent(unittest.TestCase):
    def testNotDefined(self):
        self.assertRaises(cotg(0))
        self.assertRaises(cotg(180))

    def testInteger(self):
        self.assertAlmostEqual(cotg(45), 1)
        self.assertAlmostEqual(cotg(135), -1)
        self.assertAlmostEqual(cotg(225), 1)
        self.assertAlmostEqual(cotg(315), -1)

        self.assertAlmostEqual(cotg(221), 1.1503)
        self.assertAlmostEqual(cotg(95), -0.0874)
        self.assertAlmostEqual(cotg(72), 0.3249)

    def testFloat(self):
        self.assertAlmostEqual(cotg(320.6), -1.2174)
        self.assertAlmostEqual(cotg(182.8), 20.4464)
        self.assertAlmostEqual(cotg(82.5), 0.1316)


"""@brief: Tests for constants in functions"""
class TestConstants(unittest.TestCase):
    def testPi(self):
        self.assertAlmostEqual(pi, 3.14159265359)

        self.assertAlmostEqual(add(pi, 10), 31.4159265359)
        self.assertAlmostEqual(sub(pi, 3), 0.14159265359)

        self.assertAlmostEqual(mult(pi, 2), 6.2831)
        self.assertAlmostEqual(div(150, pi), 47.7464)

        self.assertAlmostEqual(pow(pi, 2), 9.8696)
        self.assertRaises(pow(5, pi))

        self.assertAlmostEqual(root(pi, 2), 1.7724)
        self.assertRaises(root(5, pi))

        self.assertRaises(fact(pi))

    def testE(self):
        self.assertAlmostEqual(e, 2.71828182846)

        self.assertAlmostEqual(add(e, 10), 27.1828182846)
        self.assertAlmostEqual(sub(e, 2), 0.71828182846)

        self.assertAlmostEqual(mult(e, 2), 5.4365)
        self.assertAlmostEqual(div(150, e), 55.1819)

        self.assertAlmostEqual(pow(e, 2), 7.389)
        self.assertRaises(pow(5, e))

        self.assertAlmostEqual(root(e, 2), 1.6487)
        self.assertRaises(root(5, e))

        self.assertRaises(fact(e))


if __name__ == '__main__':
    unittest.main()
    print("All tests passed")
