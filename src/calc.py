"""!
@file calc.py
@brief Processing script for computing the result of input
@author Matej Hložek, xhloze02, PyJaMa's
@date March/April/May 2021
"""
import Math_lib as Math     # imports our math library as 'Math' for easier typing
##@param signs
#Global array with sign characters
signs = ["+", "-", "*", "/", "^", "√", "!"]


def get_pars(eq: str):
    """!get_pars
    @brief Gets indexes of the largest couple of parentheses
    @param eq A string to get indexes from
    @return [index of 1st, index of 2nd] parentheses or Error string"""

    front = 0   # the number of opening parentheses
    end = 0     # the number of closing parentheses
    first = -1  # the index of first opening parenthesis
    last = -1   # the index of last closing parenthesis

    i = 0   # iterator index
    for char in eq:
        # for every character in equation check:

        if char == "(":
            # check if character is starting parenthesis
            if first == -1:
                first = i       # marks the first opening parenthesis
            front += 1          # opening parentheses counter +1
        elif char == ")":
            # checks if character is closing parenthesis
            if (front - 1) == end:
                # checks if the current parenthesis is the last closing parenthesis
                last = i        # marks the last closing parenthesis
                return [int(first), int(last)]  # returns the indexes
            else:
                end += 1        # closing parentheses counter +1
        i += 1
    if front != end:
        # checks if the number of opening and closing parentheses is equal
        return ["error", "error"]   # returns error signal


def rewrite(eq: list, index: int, insert):
    """!rewrite
    @brief Reconstructs the list with result of calculation
    @param eq A list to reconstruct
    @param index Index where should the variable "insert" should be inserted (integer)
    @param insert A variable to be inserted onto desired index
    @return A updated list with result of calculation"""

    ret = eq[:index - 1]        # gets equation from beginning to index-1 and stores it to returning
    ret.append(insert)          # concatenates the inserted variable to returning
    ret.extend(eq[index + 2:])  # concatenates the rest of needed equation to returning
    return ret                  # returns changed equation


def to_list(eq: str):
    """!to_list
    @brief Converts string into list of numbers and operators
    @param eq A string to make a list from
    @return A list of numbers and operators"""

    num = " "       # declaration of number
    final = []      # declaration of final returning list

    i = 1           # iterator index
    for char in eq:
        # for every character in equation check:

        if char in signs:
            # if the character is in global list
            final.append(num.strip())       # adds number as new element to final list
            final.append(char)              # adds sign as new element to final list
            num = " "                       # clears the number variable
        else:
            num += (str(char))              # concatenates the number with character
            if len(eq) == i:
                # if this is the last character
                final.append(num.strip())   # adds number as last element to final list
        i += 1

    eq = final  # stores final list backs to equation
    return eq   # returns completed list


def check_empty(eq: str):
    """!check_neg
    @brief Checks if input variable does include empty string or an negative number and repairs it
    @param eq A iterable variable to be checked (string or list)
    @return A repaired (if needed) list without empty strings and wrongly written negative numbers"""

    i = 0       # iterator index
    for elem in eq:
        # for every element in equation list
        if elem is None or elem == "" or elem in signs:
            # if element is NULL
            if len(eq) > i + 1:
                # check so it won't reach out of equation list
                # checks for finding and deleting the NULL element:
                if eq[i + 1] == "-":
                    num = type_check(eq[i + 2]) * (-1)
                    del eq[i + 1]
                    del eq[i]
                    eq[i] = num
                if eq[i - 1] == "!":
                    del eq[i]
        i += 1
    return eq   # returns the repaired list
    # this works but it could be done way better, i just don't want to break whole code


def type_check(num: str):
    """!type_check
    @brief Checks type of input number and coverts it into adequate type
    @param num A number to convert (string)
    @return A number (either float or integer depending on input number) """

    if not num:
        # if number is NULL
        return
    elif type(num) is str:
        # if number is string type
        if "." in num:
            # if it has floating point
            num = float(num)        # retypes the number to float
            num = defloat(num)      # checks if it can be retyped to integer
        else:
            num = int(num)          # retypes the number to integer
    return num  # returns the retyped number


def check_gon(eq):
    """!check_gon
    @brief Checks if there are goniometric functions in input variable and calculates them
    @param eq A list to check
    @return List without goniometric functions"""

    i = 0   # iterator index
    for elem in eq:
        # for every element in equation list check
        if type(elem) == str:
            # if the element is string type
            if "sin" in elem:
                # sine
                num = float(elem[3:])               # retypes the number to float
                eq[i] = defloat(Math.sin(num))      # solves the sine and returns the solution
            elif "cos" in elem:
                # cosine
                num = float(elem[3:])               # retypes the number to float
                eq[i] = defloat(Math.cos(num))      # solves the cosine and returns the solution
            elif "tan" in elem:
                # tangent
                num = float(elem[3:])               # retypes the number to float
                eq[i] = defloat(Math.tan(num))      # solves the tangent and returns the solution
            elif "cotg" in elem:
                # cotangent
                num = float(elem[4:])               # retypes the number to float
                eq[i] = defloat(Math.cotg(num))     # solves the cotangent and returns the solution
        i += 1
    return eq   # returns equation with solved goniometric functions


def findC(eq: str, sign: str):
    """!findC
    @brief Finds first occurrence of given variable
    @param eq  A iterable variable where the character will be searched (string or list)
    @param sign A variable to be searched (string)
    @return An index of occurrence of character"""

    i = 0   # iterator index
    for char in eq:
        if char == sign:
            return i    # returns the index of wanted sign
        i += 1


def defloat(num):
    """!defloat
    @brief Check if the number can be retyped to integer
    @param num A number to be checked (float or integer)
    @return Either unchanged float number or integer number"""

    if type(num) == float:
        # if number is float type
        num = str(num)  # retype float number to string
        if num[len(num)-1] == "0" and num[len(num)-2] == ".":
            # if it can be retyped to integer ( the second last element is '.' and the last is zero)
            num = int(float(num))   # retypes number to integer
            return num
        else:
            num = float(num)    # retypes number to float
            return num
    return num


def calculate(eq: str):
    """!calculate
    @brief The main function to process given equation
    @param eq String to calculate
    @return A result"""

    try:
        # try looks for any exception, if any is encountered jumps to 'except'
        while "(" in eq:
            # while there are unsolved parentheses, try to solve them
            x, y = get_pars(eq)
            if x == "error" or y == "error":
                return "error"
            eq = eq[:x] + defloat(calculate(eq[(x + 1): y])) + eq[y + 1:]

        eq = to_list(eq)        # converts string to list
        eq = check_empty(eq)    # repairs list if needed
        eq = check_gon(eq)      # solves goniometric functions
        index = 0
        while "+" in eq or "-" in eq or "*" in eq or "/" in eq or "^" in eq or "√" in eq or "!" in eq:
            #  while there are operators in equation, try solve it
            if "error" in eq:
                # if any error occurred before solving current equation return 'error' as result
                return "error"

            elif "!" in eq:
                # factorial
                index = findC(eq, "!")              # finds the factorial sign
                num = type_check(eq[index - 1])     # retypes the number
                res = Math.fact(num)                # solves the factorial
                eq[index - 1] = res                 # rewrites the element on index of the number with result
                del eq[index]                       # deletes the factorial sign form equation

            elif "^" in eq:
                # power
                index = findC(eq, "^")              # finds the power sign
                num1 = type_check(eq[index-1])      # retypes the first number (base)
                num2 = type_check(eq[index+1])      # retypes the second number (exponent)
                res = Math.pow(num1, num2)          # solves the power
                eq = rewrite(eq, index, res)        # rewrites the equation

            elif "√" in eq:
                # root
                index = findC(eq, "√")              # finds the root sign
                num1 = type_check(eq[index - 1])    # retypes the first number (exponent)
                num2 = type_check(eq[index + 1])    # retypes the second number (base)
                res = Math.root(num2, num1)         # solves the equation
                eq = rewrite(eq, index, res)        # rewrites the equation

            elif "/" in eq:
                # division, but it will be changed to multiplication as '1 divided by number'
                index = findC(eq, "/")              # finds the division sign
                eq[index] = "*"                     # changes the division sign to multiplication
                num = type_check(eq[index + 1])     # retypes the number
                num = Math.div(1, num)              # solves the '1 divided by number'
                eq[index + 1] = num                 # rewrites the number

            elif "*" in eq:
                # multiplication
                index = findC(eq, "*")              # finds the multiplication sign
                num1 = type_check(eq[index - 1])    # retypes the first number
                num2 = type_check(eq[index + 1])    # retypes the second number
                res = Math.mult(num1, num2)         # solves the multiplication
                eq = rewrite(eq, index, res)        # rewrites the equation

            elif "-" in eq:
                # subtraction, but it will be changed to addition of negative number
                index = findC(eq, "-")              # finds the negation sign
                eq[index] = "+"                     # changes the sign to plus
                num = type_check(eq[index+1])*(-1)  # changes the number to negative and retypes it
                eq[index + 1] = num                 # rewrites the original number with negative one

            elif "+" in eq:
                # addition
                index = findC(eq, "+")              # finds the plus sign
                num1 = type_check(eq[index - 1])    # retypes the first number
                if num1 is None:
                    # checks if for some unknown reason the first number is None
                    num1 = 0
                num2 = type_check(eq[index + 1])    # retypes the second number
                res = Math.add(num1, num2)          # solves the addition
                eq = rewrite(eq, index, res)        # rewrites the equation

        res = eq[0]             # stores the final result
        if type(res) == float:
            # if result is float rounds it
            res = round(res, Math.d_digits-1)

        return str(res)         # returns the result as string

    except:
        # if any error occurred returns 'error' as result
        return "error"


def evaluate(eq: str):
    """!evaluate
    @brief connecting function for GUI
    @param eq String to calculate
    @return a result or an error string"""

    eq = calculate(eq)          # calls the 'main' function

    if "error" == eq:
        # if any error occurred during the calculations returns error string
        return "Math Error"

    eq = str(defloat(float(eq)))     # checks if the value can be changed from float to integer
    return eq                   # returns the final solution
