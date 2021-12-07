from day1 import categorize_measurements
from day1 import sliding_window

data_to_try = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263, 270]
result = ["increased", "increased", "increased", "decreased", "increased", "increased", "increased", "decreased", "increased"]

def test_measurements():
    assert categorize_measurements(data_to_try), 8

def test_sling_window():
    assert sliding_window(data_to_try), 6