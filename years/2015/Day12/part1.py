# COMPLETED

import json
import os

def find_numbers(obj):
    integers = [] # Full list of integers
    if isinstance(obj, int): # If integer, append to the list
        integers.append(obj)
    elif isinstance(obj, list): # If list, iterate over each item
        for item in obj:
            integers.extend(find_numbers(item)) # Extend because recursion
    elif isinstance(obj, dict):
        for value in obj.values():
            integers.extend(find_numbers(value)) # Extend because recursion
    return integers


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.read()
    data_json = json.loads(data)

    print("PART ONE:")
    tests = [
        '[1,2,3]',
        '{"a":2, "b": 4}',
        '[[[3]]]',
        '{"a":{"b":4},"c":-1}',
        '{"a":[-1,1]}',
        '[-1,{"a":1}]',
        '[]',
        '{}'
    ]
    for test in tests:
        test_json = json.loads(test)
        numbers = find_numbers(test_json)
        sum_numbers = sum(numbers)
        print(f"Test: {test} -> sum: {sum_numbers}")
    numbers = find_numbers(data_json)
    sum_numbers = sum(numbers)
    print(f"Sum of all numbers: {sum_numbers}")
