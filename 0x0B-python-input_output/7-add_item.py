#!/usr/bin/python3
"""
A script that adds all arguments to a Python list, and then save them to a file
"""
import sys

if __name__ == "__main__":
    """
    Save json file import
    """
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    """
    Load json file import
    """
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    """
    Save json data filename
    """
    filename = "add_item.json"
    items = []
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
