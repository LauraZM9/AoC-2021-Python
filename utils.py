# get data

import csv
import os

def read_data(day):
    DATA_PATH = os.path.join("data", "2021_{}.csv".format(day))
    data = list()
    with open(DATA_PATH, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row[0])
    return data

