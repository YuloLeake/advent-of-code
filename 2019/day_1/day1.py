""" Day 1: The Tyranny of the Rocket Equation

Part 1: Fule = floor(mass / 3) - 2.
Part 2: Need a fuel for the added mass of fuel, and so on.
"""
import math

def fuel(mass: int):
    return math.floor(mass / 3) - 2


def fuel_for_fuel(mass: int):
    if mass == 0:
        return 0
    mass_of_fuel = max(fuel(mass), 0)
    return mass_of_fuel + fuel_for_fuel(mass_of_fuel)



if __name__ == '__main__':
    # Part 1
    with open('modules.txt', 'r') as f:
        modules = f.readlines()

    fuel_required = sum(fuel(int(mass)) for mass in modules)
    print(fuel_required)

    # Part 2
    fuel_required = sum(fuel_for_fuel(int(mass)) for mass in modules)
    print(fuel_required)