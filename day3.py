""" Solution for day 3 of 2021 Advent of Code """

from utils import read_data

data = read_data("03")

def get_power_consumption(diagnostic:list) -> int:
    """Power consumption
    """
    gamma = ""
    epsilon = ""
    for i in range(len(diagnostic[0])):
        ones = 0
        for num in diagnostic:
            if num[i] == "1":
                ones += 1
        if ones > len(diagnostic)//2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

print(get_power_consumption(data))

def get_life_support_rating(diagnostic:list) -> int:
    """ Life support rating
    """
    o2_generator = ""
    co2_scrubber = ""
    return 0