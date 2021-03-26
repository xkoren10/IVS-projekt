## @file: Math_lib.py
# @brief: Implementation of mathematical functions and constants
# @author: Marek Tiss, xtissm00, PyJaMa's
# @date: March 2021 

import math

## @var pi
# Constant pi
pi = 3.14159265359
## @var e
#Constant e
e = 2.71828182846
## @var d_digits
# Number of decimal digits:
d_digits = 10

## Addition
# @brief Adds 2 numbers together (x+y)
# @param x First number
# @param y Second number
# @return Sum of x and y
def add(x, y):
    return x + y

## Substraction
# @brief Substracts number y from number x (x-y)
# @param x First number
# @param y Second number
# @return Difference of x and y
def sub(x, y):
    return x - y

## Multiplication
# @brief Multiplies numbers x and y (x*y)
# @param x First number
# @param y Second number
# @return Product of x and y
def mult(x, y):
    return round(x * y, d_digits)

## Division
# @brief Divides number x by number y (x/y)
# @param x Divident
# @param y Divisor
# @return Quotient of x and y
# @exception ZeroDivisionError if y = 0
def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by 0!")    
    return round(x / y, d_digits)

## Exponentiation
# @brief Raises number x to the power of n (x^n)
# @param x Base number
# @param n Exponent
# @return X to the power of n
# @exception ValueError if n isn't natural number
def pow(x, n):
    if (isinstance(n, int) and n >= 0):
        return round(x ** n, d_digits)
    raise ValueError("Exponent must be a natural number!")

## Root
# @brief Calculates n-th root of number x
# @param x Base number
# @param n Order of the root
# @return N-th root of x
# @exception ValueError if n isn't natural number
# @exception ValueError if x is negative and n is even
def root(x, n):
    if (isinstance(n,int) and n > 0):
        if ( x >= 0 or n % 2 == 1 ):
            n = div(1.0,n)
            if x >= 0:
                return round((x ** n), d_digits)
            else:
                return round(-((-x)**n), d_digits)
        raise ValueError("Negative number can't have an even order of the root!")
    raise ValueError("Exponent must be natural number!")


## Factorial
# @brief Calculates factorial of number x (x!)
# @param x Number
# @return Factorial of x 
# @exception ValueError if x isn't natural number
def fact(x):
    if (isinstance(x,int) and x > 0):
        return (math.factorial(x))

    raise ValueError("Exponent must be a natural number!")

## Sine
# @brief Calculates sine of number x (opposite/hypotenuse)
# @param x Number in degrees
# @return Sine of x
def sin(x):
    x = div(mult(x, pi), 180)
    return round(math.sin(x), d_digits)

## Cosine
# @brief Calculates cosine of number x (adjacent/hypotenuse)
# @param x Number in degrees
# @return Cosine of x
def cos(x):
    x = div(mult(x, pi), 180)
    return round(math.cos(x), d_digits)

## Tangent
# @brief Calculates tangent of number x (opposite/adjacent)
# @param x Number in degrees
# @return Tangent of x
# @exception ValueError if x is 90 + 180*I, while I is whole number
def tan(x):
    if (x % 180 == 90 or x % 180 == -90):
        raise ValueError("Tangent doesn't exist")

    x= div(mult(x, pi), 180)
    return round(math.tan(x), d_digits)

## Cotangent
# @brief Calculates cotangent of number x (adjacent/opposite)
# @param x Number in degrees
# @return coangent of x
# @exception ValueError if x is 180*I, while I is whole number
def cotg(x):
    if (x % 180 == 0):
        raise ValueError("Cotangent doesn't exist")

    return round(tan(x)**-1, d_digits)