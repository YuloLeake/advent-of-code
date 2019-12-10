from typing import NamedTuple
import unittest

from day4 import is_ascending, is_valid_pw, meets_part_2

class Example(NamedTuple):
    password: str
    is_valid: bool

class TestDay4(unittest.TestCase):

    def test_part_1(self):
        test_cases = [
            Example('111111', True),
            Example('111123', True),
            Example('135679', False),
            Example('122345', True),
            Example('223450', False),
            Example('123789', False)
        ]
        
        for case in test_cases:
            pw = case.password
            is_valid = is_ascending(pw) and is_valid_pw(pw)
            self.assertEqual(is_valid, case.is_valid)


    def test_part_2(self):
        test_cases = [
            Example('112233', True),
            Example('123444', False),
            Example('111122', True), # 1111 is bad, but 22 is good, so good
            Example('111123', False) # 1111 is bad, no good adjacent
        ]
        
        for case in test_cases:
            pw = case.password
            is_valid = is_ascending(pw) and is_valid_pw(pw) and meets_part_2(pw)
            self.assertEqual(is_valid, case.is_valid)

if __name__ == '__main__':
    unittest.main()