#!/usr/bin/python3
"""script to load json to list and save to file"""
import sys

save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    my_list = []

    try:
        my_list = load_json('dd_item.json')
    except FileNotFoundError:
        my_list = []

    my_list.append(sys.argv[1:])
    save_json(my_list)
