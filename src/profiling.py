"""
 @file: profiling.py
 @brief: Profiling of Math_lib
 @author: Matej Koren, xkoren10, PyJaMa's
 @date: 16 April 2021

"""


import Math_lib
from random import random
import sys
import cProfile


def generate_random_numbers(number):

    path = 'rng1000.txt'

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
    count = 0
    up_sum = 0

    with open(path) as infile:
        for line in infile:
            num = float(line)
            sum_of_values = Math_lib.add(sum_of_values, num)
            count = count + 1

    avg_of_values = Math_lib.div(sum_of_values, count)

    with open(path) as infile:
        for line in infile:
            num = float(line)
            up_sum = Math_lib.add(up_sum, Math_lib.pow(Math_lib.sub(num, avg_of_values), 2))

    dev = Math_lib.root(Math_lib.div(up_sum, count-1), 2)

    print(dev)

    return


if sys.stdin.isatty():
    generate_random_numbers(1000)
    cProfile.run('deviation("rng1000.txt")')
    """deviation("rng1000.txt")"""
else:
    with open("test.txt", "w") as file:
        file.write(sys.stdin.read())
        file.close()
    path = 'test.txt'

    cProfile.run('deviation(path)')
"""deviation(path)"""
