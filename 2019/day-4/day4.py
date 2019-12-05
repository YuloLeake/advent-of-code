""" Day 4: Secure Container

Valid password criteria:
  1. It is a six-digit number.
  2. Two adjacent digits are the same (like 22 in 122345).
  3. The value is within the range given in your puzzle input.
  4. Going from left to right, the digits never decrease; they only ever 
      increase or stay the same (like 111123 or 135679).
  5. Two adjacent matching digits are not part of a larger group of matching 
      digits. (only for part 2)
"""
from itertools import groupby

def is_ascending(password: str) -> bool:
    # Criteria 4
    return ''.join(sorted(password)) == password


def is_valid_pw(password: str) -> bool:
    """ Whether given password is valid or not.

    Covers criteria 1 and 2.
    Also covers criteria 5 when part_2 is True
    """
    # criteria 1
    is_six_digit = len(password) == 6

    # criteria 2
    adjacents = [''.join(group) for _, group in groupby(password)]
    adjacents = [adj for adj in adjacents if len(adj) > 1]
    has_good_adjacent = len(adjacents) > 0

    return is_six_digit and has_good_adjacent


def meets_part_2(password: str) -> bool:
    """ Check whether given password meets Criteria 5 (part 2). """
    adjacents = [''.join(group) for _, group in groupby(password)]
    adjacents = [adj for adj in adjacents if len(adj) == 2] # Criteria 5
    return len(adjacents) > 0


if __name__ == '__main__':
    # Part 1
    start = 158126
    end   = 624574
    pws = 0
    for i in range(start, end+1): # Criteria 3
        pw = str(i)
        is_valid = is_ascending(pw) and is_valid_pw(pw)
        pws += 1 if is_valid else 0
    print(f'part 1 = {pws}')

    # Part 2
    start = 158126
    end   = 624574
    pws = 0
    for i in range(start, end+1): # Criteria 3
        pw = str(i)
        is_valid = is_ascending(pw) and is_valid_pw(pw) and meets_part_2(pw)
        pws += 1 if is_valid else 0
    print(f'part 2 = {pws}')