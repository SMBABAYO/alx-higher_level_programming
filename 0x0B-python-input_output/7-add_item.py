#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        with open(filename, 'r') as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    with open(filename, 'w') as file:
        json.dump(items, file)
