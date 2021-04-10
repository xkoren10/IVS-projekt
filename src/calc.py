"""
@file: calc.py
@brief: Processing script for computing the result of input
@author: Matej Hložek, xhloze02, PyJaMa's
@date: March/April 2021
"""
import Math_lib as Math


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


def rewrite(eq: str, index: int, insert):
    """rewrite
    @brief: Reconstructs the list with result of calculation
    @type eq: String or list
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

    signs = ["+", "-", "*", "/"]
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
    index = 0
    while "+" in eq or "-" in eq or "*" in eq or "/" in eq:
        if "*" in eq:
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

        elif "+" in eq:
            index = findC(eq, "+")
            num1 = type_check(eq[index - 1])
            num2 = type_check(eq[index + 1])
            res = Math.add(num1, num2)
            eq = rewrite(eq, index, res)

        elif "-" in eq:
            index = findC(eq, "-")
            num1 = type_check(eq[index - 1])
            num2 = type_check(eq[index + 1])
            res = Math.sub(num1, num2)
            eq = rewrite(eq, index, res)

    return str(eq[0])


def evaluate(eq: str):
    """evaluate
    @brief: connecting function for GUI
    @type eq: string
    @param eq: String to calculate
    @rtype: string
    @return: a result"""

    eq = calculate(eq)
    return str(eq)
