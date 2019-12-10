from typing import NamedTuple, List
import unittest

from day1 import frequency, first_repeat

class Example(NamedTuple):
    values: List[str]
    frequency: int

class TestDay1(unittest.TestCase):

    def test_part_1(self):
        test_cases = [
            Example(['+1', '-2', '+3', '+1'], 3),
            Example(['+1', '+1', '+1'], 3),
            Example(['+1', '+1', '-2'], 0),
            Example(['-1', '-2', '-3'], -6)
        ]
        
        for case in test_cases:
            values = case.values
            self.assertEqual(frequency(values), case.frequency)


    def test_part_2(self):
        test_cases = [
            Example(['+1', '-2', '+3', '+1'], 2),
            Example(['+1', '-1'], 0),
            Example(['+3', '+3', '+4', '-2', '-4'], 10),
            Example(['-6', '+3', '+8', '+5', '-6'], 5),
            Example(['+7', '+7', '-2', '-7', '-4'], 14)
        ]

        for case in test_cases:
            values = case.values
            self.assertEqual(first_repeat(values), case.frequency)

if __name__ == '__main__':
    unittest.main()