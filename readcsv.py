import csv

def read_csv():
    with open('data.csv', 'rt') as f:
        data = csv.reader(f)
        for row in data:
            print(row)
    return data

read_csv()