from utils import read_data

# data is a list of strings
data = read_data('01')

def categorize_measurements(measurements: list) -> list:
    increased = 0
    for i in range(0, len(measurements) - 1):
        if int(measurements[i]) < int(measurements[i + 1]):
            increased += 1
    return increased

# print(categorize_measurements(data))

def sliding_window(measurements: list) -> list:
    new_measurements = []
    for i in range(0, len(measurements) - 2):
        new_measurements.append(int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2]))
    increased = categorize_measurements(new_measurements)
    return increased

# print(sliding_window(data))