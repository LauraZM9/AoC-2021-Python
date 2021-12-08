from day1 import categorize_measurements, get_sliding_window
from day2 import get_final_position, get_correct_position
from day3 import get_life_support_rating, get_power_consumption


# Tests day 1
data_to_try = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263, 270]

def test_measurements():
    assert categorize_measurements(data_to_try), 8

def test_sling_window():
    assert get_sliding_window(data_to_try), 6


# Tests day 2
instructions = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def test_position():
    assert get_final_position(instructions), 150

def test_correct_position():
    assert get_correct_position(instructions), 900


# Tests day 3
diagnostic_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def test_power_consumption():
    assert get_power_consumption(diagnostic_report), 198

def test_life_support_rating():
    assert get_life_support_rating(diagnostic_report), 230