from csv import reader

def read_csv(this_file):
    with open(this_file, 'r') as f:
        data = reader(f)
        for row in data:
            tuple_list = list(map(tuple, data))
            print(tuple_list)
    return data

read_csv('data.csv')