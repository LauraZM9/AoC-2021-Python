""" Solution for day 1 from 2021 Advent of Code """
from utils import read_data

# data is a list of strings
data = read_data("01")


def categorize_measurements(measurements: list) -> int:
    """Returns the number of times the measurement increased compared with the previous one.

    Args:
        measurements (list): list of measurements in the form of strings

    Returns:
        increased (int): the number of times the measurement increased
    """

    increased = 0
    for i in range(0, len(measurements) - 1):
        if int(measurements[i]) < int(measurements[i + 1]):
            increased += 1
    return increased


# print(categorize_measurements(data))


def sliding_window(measurements: list) -> int:
    """Calculates a sliding window of three measurements and then returns the number of times the measurement increased compared with previous

    Args:
        measurements (list): list of measurements (strings)

    Returns:
        increased(int): the number of times the measurement increased
    """

    new_measurements = []
    for i in range(0, len(measurements) - 2):
        new_measurements.append(
            int(measurements[i]) + int(measurements[i + 1]) + int(measurements[i + 2])
        )
    return new_measurements


print(categorize_measurements(sliding_window(data)))
