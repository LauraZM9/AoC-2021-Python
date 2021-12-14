""" Solution for day 3 of 2021 Advent of Code """

from utils import read_data

data = read_data("03")

def get_most_common_bit(diagnostic:list, position:int) -> str:
    ones = 0
    for num in diagnostic:
        if num[position] == "1":
            ones += 1
    if ones >= len(diagnostic)/2:
        return "1"
    else:
        return "0"

def get_least_common_bit(diagnostic:list, position:int) -> str:
    ones = 0
    for num in diagnostic:
        if num[position] == "1":
            ones += 1
    if ones >= len(diagnostic)/2:
        return "0"
    else:
        return "1"

def get_power_consumption(diagnostic:list) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(diagnostic[0])):
        gamma += get_most_common_bit(diagnostic, i)
        epsilon += get_least_common_bit(diagnostic, i)
    return int(gamma, 2) * int(epsilon, 2)

print(get_power_consumption(data))

def filter_most_common_bit(diagnostic:list) -> str:
    for i in range(len(diagnostic[0])):
        diagnostic = [x for x in diagnostic if x[i] == get_most_common_bit(diagnostic, i)]
        if len(diagnostic) == 1:   
            break
    return diagnostic[0]

def filter_least_common_bit(diagnostic:list) -> str:
    for i in range(len(diagnostic[0])):
        diagnostic = [x for x in diagnostic if x[i] == get_least_common_bit(diagnostic, i)]
        if len(diagnostic) == 1:   
            break
    return diagnostic[0]

def get_life_support_rating(diagnostic:list) -> int:
    o2 = filter_most_common_bit(diagnostic)
    co2 = filter_least_common_bit(diagnostic)
    return int(o2, 2) * int(co2, 2)

print(get_life_support_rating(data))
