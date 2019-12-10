""" Day 1: The Tyranny of the Rocket Equation

Part1: Fule = floor(mass / 3) - 2
"""
import math
from typing import List

def fuel(mass: int):
    return math.floor(mass / 3) - 2



if __name__ == '__main__':
    # Part 1
    with open('sequence.txt', 'r') as f:
        modules = f.readlines()
