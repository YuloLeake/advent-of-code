from typing import NamedTuple, List
import unittest

from day1 import fuel, fuel_for_fuel

class Example(NamedTuple):
    mass: int
    fuel: int

class TestDay1(unittest.TestCase):

    def test_part_1(self):
        test_cases = [
            Example(12, 2),
            Example(14, 2),
            Example(1969, 654),
            Example(100756, 33583)
        ]
        
        for case in test_cases:
            self.assertEqual(fuel(case.mass), case.fuel)


    def test_part_2(self):
        test_cases = [
            Example(12, 2),
            Example(14, 2),
            Example(1969, 966),
            Example(100756, 50346)
        ]
        
        for case in test_cases:
            self.assertEqual(fuel_for_fuel(case.mass), case.fuel)

if __name__ == '__main__':
    unittest.main()