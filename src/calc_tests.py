"""!
@file calc_tests.py
@brief Tests for calc.py
@author Matej Hložek, xhloze02, PyJaMa's
@date March 2021
"""

import unittest
import calc


def test_ok(test_name: str):
    """!@brief Test control"""
    print("Test {}: ok".format(test_name))


class TestBasics(unittest.TestCase):
    """!@brief Tests for basic calculations with one kind of operators"""
    def testOneNumber(self):
        """!@brief Test for the return of a single number"""
        self.assertEqual(calc.evaluate("1"), "1")
        self.assertAlmostEqual(float(calc.evaluate("150.7")), 150.7)

        test_ok("One Number")

    def testAdd(self):
        """!@brief Test for the addition"""
        self.assertEqual(calc.evaluate("1+2+3+4+5"), "15")
        self.assertAlmostEqual(float(calc.evaluate("4.5+8.65+7.23")), 20.38)

        test_ok("Basic addition")

    def testSub(self):
        """!@brief Test for the subtraction"""
        self.assertEqual(calc.evaluate("10-7-1"), "2")
        self.assertAlmostEqual(float(calc.evaluate("-2.4-4.7-1.1-5.3")), -13.5)

        test_ok("Basic subtraction")

    def testMultiplication(self):
        """!@brief Test for the multiplication"""
        self.assertEqual(calc.evaluate("5*2*-7"), "-70")
        self.assertAlmostEqual(float(calc.evaluate("1.1*4.3*3.6")), 17.028)

        test_ok("Basic Multiplication")

    def testDivision(self):
        """!@brief Test for the division"""
        self.assertAlmostEqual(float(calc.evaluate("150/8/3")), 6.25)
        self.assertAlmostEqual(float(calc.evaluate("858.0/2.5/1.5")), 228.8)

        test_ok("Basic division")

    def testPower(self):
        """!@brief Test for the power of a given number"""
        self.assertEqual(calc.evaluate("5^2"), "25")
        self.assertAlmostEqual(float(calc.evaluate("5.2^3")), 140.608)

        test_ok("Basic power")

    def testRoot(self):
        """!@brief Test for the square root of a given number"""
        self.assertEqual(calc.evaluate("2√9"), "3")
        self.assertAlmostEqual(float(calc.evaluate("2√30.25")), 5.5)

        test_ok("Basic root")

    def testFactorial(self):
        """!@brief Test for the factorial of a given number"""
        self.assertEqual(calc.evaluate("5!"), "120")

        test_ok("Basic factorial")


class TestGoniometric(unittest.TestCase):
    """!@brief Tests for calculations of goniometric functions"""
    def testSine(self):
        """!@brief Test for the sine value of a given number (in degrees)"""
        self.assertEqual(calc.evaluate("sin(90)"), "1")
        test_ok("Sine")

    def testCosine(self):
        """!@brief Test for the cosine value of a given number (in degrees)"""
        self.assertEqual(calc.evaluate("cos(90)"), "0")
        test_ok("Cosine")

    def testTangent(self):
        """!@brief Test for the tangent value of a given number (in degrees)"""
        self.assertEqual(calc.evaluate("tan(180)"), "0")
        test_ok("Tangent")

    def testCotangent(self):
        """!@brief Test for the cotangent value of a given number (in degrees)"""
        self.assertEqual(calc.evaluate("cotan(45)"), "1")
        test_ok("Cotangent")


class TestMultipleOperators(unittest.TestCase):
    """!@brief Test for calculations with multiple different operators"""
    def testBasicOperators(self):
        """!@brief Test for calculations with different simple operators"""
        self.assertEqual(calc.evaluate("2+2-8"), "-4")
        self.assertEqual(calc.evaluate("-5+7-2+1"), "1")
        self.assertEqual(calc.evaluate("2*5+9-4"), "15")
        self.assertAlmostEqual(float(calc.evaluate("8+3-5*3.5")), -6.5)
        self.assertAlmostEqual(float(calc.evaluate("94/2+5-9.2")), 42.8)
        self.assertAlmostEqual(float(calc.evaluate("5*6/8+5")), 8.75)
        self.assertAlmostEqual(float(calc.evaluate("2-7*4+9.6/4")), -23.6)

    test_ok("Multiple basic operators")

    def testAdvancedOperators(self):
        """!@brief Test for calculations with different advanced operators"""
        self.assertEqual(calc.evaluate("2√16+5-4*2"), "1")
        self.assertEqual(calc.evaluate("5!/10+5*1"), "17")
        self.assertEqual(calc.evaluate("2^2*2+2/2"), "9")
        self.assertEqual(calc.evaluate("2√4^4+2"), "18")

    test_ok("Multiple advanced operators")


class TestParentheses(unittest.TestCase):
    """!@brief Tests for calculations with parentheses"""
    def testBasicOperators(self):
        """!@brief Tests for calculations with parentheses and different simple operators"""
        self.assertAlmostEqual(float(calc.evaluate("3*(2+4-1)/2")), 7.5)
        self.assertAlmostEqual(float(calc.evaluate("-4*(4/5+2)")), -11.2)
        self.assertAlmostEqual(float(calc.evaluate("(2+6*2)+(2/4+5)")), 19.5)
        self.assertEqual(calc.evaluate("(5+7+3+9)/(2^2)"), "6")
        self.assertEqual(calc.evaluate("(1+(1+2)+2)+3"), "9")
        self.assertEqual(calc.evaluate("4/(1+6-3)"), "1")

        test_ok("Basic parentheses")

    def testAdvancedOperators(self):
        """!@brief Tests for calculations with parentheses and different advanced operators"""
        self.assertEqual(calc.evaluate("2^(1+2/2+2)"), "16")
        self.assertEqual(calc.evaluate("2√(5+3-2*2)"), "2")
        self.assertAlmostEqual(float(calc.evaluate("3√(3*3+30-12)")), 3)
        self.assertAlmostEqual(float(calc.evaluate("(9*100+6*10+10-10)/5!")), 8)
        self.assertEqual(calc.evaluate("(5*5/10*2)^(5-3*2+6)"), "3125")
        self.assertAlmostEqual(float(calc.evaluate("(9*(5^2-10)/9)/2")), 7.5)

        test_ok("Advanced parentheses")


class TestErrors(unittest.TestCase):
    """!@brief Tests for error handling"""
    def testErrors(self):
        """!@brief Tests for Math errors"""
        self.assertEqual(calc.evaluate("5/0"), "Math Error")
        self.assertEqual(calc.evaluate("2^2.2"), "Math Error")
        self.assertEqual(calc.evaluate("2^-2"), "Math Error")
        self.assertEqual(calc.evaluate("-5√2"), "Math Error")
        self.assertEqual(calc.evaluate("2.2√2"), "Math Error")
        self.assertEqual(calc.evaluate("2√-4"), "Math Error")
        self.assertEqual(calc.evaluate("-5!"), "Math Error")
        self.assertEqual(calc.evaluate("4.5!"), "Math Error")
        self.assertEqual(calc.evaluate("tan(90)"), "Math Error")
        self.assertEqual(calc.evaluate("cotan(0)"), "Math Error")
        self.assertEqual(calc.evaluate("5+(5+(5)"), "Math Error")

        test_ok("Error handling")


if __name__ == '__main__':
    unittest.main()