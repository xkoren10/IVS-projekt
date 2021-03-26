"""
 @file: profiling.py
 @brief: Implementation of mathematical functions and constants
 @author: Matej Koren, xkoren10, PyJaMa's
 @date: March 2021

"""


import Math_lib
from random import random
import cProfile
import sys


def generate_random_numbers(number):

    path = 'data1000.txt'

    try:
        numbers_file = open(path, 'w')
    except IOError:
        print("Can't open file")
        exit(2)

    max_n = 1000
    min_n = -1000
    for a in range(number):
        numbers_file.write(str(random()*(max_n - min_n) + min_n))
        if a != (number-1):
            numbers_file.write(str('\n'))

    numbers_file.close()


def deviation(path):

    sum_of_values = 0
    avg_of_values = 0
    count = 0
    up_sum = 0

    with open(path) as infile:
        for line in infile:
            num = float(line)
            sum_of_values = Math_lib.add(sum_of_values, num)
            count = count + 1

    avg_of_values = Math_lib.div(sum_of_values, count)

    print("------------STANDARD DEVIATION------------")
    print("Cnt: ", count)
    print("Sum: ", sum_of_values)
    print("Avg: ", avg_of_values)

    with open(path) as infile:
        for line in infile:
            num = float(line)
            up_sum = Math_lib.add(up_sum, Math_lib.pow(Math_lib.sub(num, avg_of_values), 2))

    division = Math_lib.div(up_sum, count-1)
    square = Math_lib.root(division, 2)

    print("-------------------------------------------")
    print("Div: ", division)
    print("-------------------------------------------")
    print("Std_dev: ", square)
    print("-------------------------------------------")
    return


print(sys.stdin.name)

if sys.stdin.isatty():
    generate_random_numbers(100)
    cProfile.run('deviation("data1000.txt")')
else:
    with open("test.txt", "w") as file:
        file.write(sys.stdin.read())
        file.close()
    path = 'test.txt'
    cProfile.run('deviation(path)')



