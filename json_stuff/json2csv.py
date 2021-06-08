import json
import csv
import pandas as pd

def make_csv(json_file, csv_file):
    df = pd.read_json(json_file)
    df.to_csv(csv_file, index = False)

make_csv('data.json', 'new.csv')