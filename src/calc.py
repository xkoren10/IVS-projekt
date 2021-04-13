"""
@file: calc.py
@brief: Processing script for computing the result of input
@author: Matej Hložek, xhloze02, PyJaMa's
@date: March/April 2021
"""
import Math_lib as Math
signs = ["+", "-", "*", "/", "^", "√"]  # array with sign characters


def get_pars(eq: str):
    """get_pars
    @brief: Gets indexes of the largest couple of parentheses
    @type eq: String
    @param eq: A string to get indexes from
    @rtype: List
    @return: [index of 1st, index of 2nd] parentheses"""

    front = 0
    end = 0
    first = -1
    last = -1
    i = 0
    for char in eq:
        if char == "(":
            if first == -1:
                first = i
            front += 1
        elif char == ")":
            if (front - 1) == end:
                last = i
                return [int(first), int(last)]
            else:
                end += 1
        i += 1


def rewrite(eq: list, index: int, insert):
    """rewrite
    @brief: Reconstructs the list with result of calculation
    @type eq: List
    @param eq: A list to reconstruct
    @type index: Integer
    @param index: Index where should the variable "insert" should be inserted
    @type insert: String or list
    @param insert: A variable to be inserted onto desired index
    @rtype: List
    @return: A updated list with result of calculation"""

    ret = eq[:index - 1]
    ret.append(insert)
    ret.extend(eq[index + 2:])
    return ret


def to_list(eq: str):
    """to_list
    @brief: Converts string into list of numbers and operators
    @type eq: String
    @param eq: A string to make a list from
    @rtype: List
    @return: A list of numbers and operators"""

    num = " "
    final = []
    i = 1
    for char in eq:
        if char in signs:
            final.append(num.strip())
            final.append(char)
            num = " "
        else:
            num += (str(char))
            if len(eq) == i:
                final.append(num.strip())
        i += 1
    eq = final
    return eq


def check_neg(eq: str):
    """check_neg
    @brief: Checks if input variable does include negative number and repairs it
    @type eq: String or list
    @param eq: A iterable variable to be checked
    @rtype: String or list
    @return: A repaired (if needed) list with corrected negative numbers"""

    i = 0
    for elem in eq:
        if elem is None or elem == "" or elem in signs:
            if eq[i+1] == "-":
                num = type_check(eq[i+2])*(-1)
                del eq[i+1]
                del eq[i]
                eq[i] = num
        i += 1
    return eq


def type_check(num: str):
    """type_check
    @brief: Checks type of input number and coverts it into adequate type
    @type num: String
    @param num: A number to convert
    @rtype: Either float or integer depending on input number
    @return: A number"""

    if not num:
        return
    elif type(num) is str:
        if "." in num:
            num = float(num)
        else:
            num = int(num)
    return num


def findC(eq: str, sign: str):
    """findC
    @brief: Finds first occurrence of given variable
    @type eq: String or list
    @param eq:  A iterable variable where the character will be searched
    @type sign: String
    @param sign: A variable to be searched
    @rtype: Integer
    @return: An index of occurrence of character"""

    i = 0
    for char in eq:
        if char == sign:
            return i
        i += 1


def defloat(num):
    """defloat
    @brief: Check if the number can be retyped to integer
    @type num: Float or integer
    @param num: A number to be checked
    @rtype: String
    @return: Either unchanged float number or integer number"""
    if type(num) == float:
        num = str(num)
        if num[len(num)-1] == "0" and num[len(num)-2] == ".":
            num = int(float(num))
            return str(num)
    return str(num)


def calculate(eq: str):
    """calculate
    @brief: The main function to process given equation
    @type eq: String
    @param eq: String to calculate
    @rtype: String
    @return: A result"""

    while "(" in eq:
        x, y = get_pars(eq)
        eq = eq[:x] + str(calculate(eq[(x + 1): y])[0]) + eq[y + 1:]

    eq = to_list(eq)
    eq = check_neg(eq)
    index = 0
    while "+" in eq or "-" in eq or "*" in eq or "/" in eq or "^" in eq or "√" in eq:
        if "^" in eq:
            index = findC(eq, "^")
            num1 = type_check(eq[index-1])
            num2 = type_check(eq[index+1])
            res = Math.pow(num1, num2)
            eq = rewrite(eq, index, res)

        elif "√" in eq:
            index = findC(eq, "√")
            num1 = type_check(eq[index - 1])
            num2 = type_check(eq[index + 1])
            res = Math.root(num2, num1)
            eq = rewrite(eq, index, res)

        elif "*" in eq:
            index = findC(eq, "*")
            num1 = type_check(eq[index - 1])
            num2 = type_check(eq[index + 1])
            res = Math.mult(num1, num2)
            eq = rewrite(eq, index, res)

        elif "/" in eq:
            index = findC(eq, "/")
            num1 = type_check(eq[index - 1])
            num2 = type_check(eq[index + 1])
            res = Math.div(num1, num2)
            eq = rewrite(eq, index, res)

        elif "-" in eq:
            index = findC(eq, "-")
            eq[index] = "+"
            num = type_check(eq[index + 1]) * (-1)
            eq[index + 1] = num

        elif "+" in eq:
            index = findC(eq, "+")
            num1 = type_check(eq[index - 1])
            if num1 is None:
                num1 = 0
            num2 = type_check(eq[index + 1])
            res = Math.add(num1, num2)
            eq = rewrite(eq, index, res)

    return str(eq[0])


def evaluate(eq: str):
    """evaluate
    @brief: connecting function for GUI
    @type eq: string
    @param eq: String to calculate
    @rtype: string
    @return: a result"""

    eq = float(calculate(eq))
    eq = defloat(eq)
    return eq
