""" Day 1: Chronal Calibration

Part1: Given a sequence of changes in frequency, solve for the resulting frequency.
"""
from typing import List

def frequency(values: List[str]):
    return sum(int(value) for value in values)


def first_repeat(values: List[str]):
    pass

if __name__ == '__main__':
    # Part 1
    with open('sequence.txt', 'r') as f:
        data = f.readlines()

    print(frequency(data))