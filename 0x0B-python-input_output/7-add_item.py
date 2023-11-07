#!/usr/bin/python3
"""
A script that adds all arguments to a Python list, and then save them to a file
"""
import sys

"""
Save json file import
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
Load json file import
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Save json data filename
"""
filename = "add_item.json"

"""
If no argument provided, fill the file with an empty list
Otherwise, add the provided arguments to the list in the file
"""
if __name__ == "__main__":
    if (len(sys.argv) == 1):
        save_to_json_file([], filename)
    else:
        for i in range(1, len(sys.argv)):
            data = sys.argv[i]
            items = load_from_json_file(filename)
            items = list(items)
            items.append(data)
            save_to_json_file(items, filename)
