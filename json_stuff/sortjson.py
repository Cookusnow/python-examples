from collections import OrderedDict 
from pprint import pprint
import argparse
import copy
import json

def sort_dict(this_dict):
    """Recursively sorts a dictionary by keys

    Args:
        this_dict (dict): a dictionary

    Returns:
        dict: a sorted dictionary
    """
    sorted = OrderedDict(this_dict)
    sorted = copy.deepcopy(sorted)
    return sorted

def read_json(this_file):
    """Reads a json file

    Args:
        this_file (str): a json file

    Returns:
        dict: a dictionary containing the json file contents
    """
    with open(this_file) as f:
        data = json.load(f)
    return data

def write_json(this_file, this_dict):
    """Writes a dictionary to a json file

    Args:
        this_file (str): target filename
        this_dict (dict): any dictionary
    """
    with open(this_file, 'w') as json_file:
        json.dump(this_dict, json_file, indent = 4, sort_keys=True)

def main():
    parser = argparse.ArgumentParser(description='Sort a json file.')
    parser.add_argument("-i", "--inputfile", type=str, help='Input File', required=True)
    parser.add_argument("-o", "--outputfile", type=str, help='Output File', required=False, default=False)

    args = parser.parse_args()
    inputFile = args.inputfile
    outputFile = args.outputfile

    jsonData = read_json(inputFile)

    sorted = sort_dict(jsonData)

    if outputFile:
        write_json(outputFile, sorted)
    else: 
        pprint(sorted)

if __name__ == "__main__":
    main()