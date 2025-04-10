# COMPLETED

import json
import os


def find_numbers(obj):
    integers = []
    if isinstance(obj, int):
        integers.append(obj)
    elif isinstance(obj, list):
        for item in obj:
            integers.extend(find_numbers(item))
    elif isinstance(obj, dict):
        if "red" in obj.values():
            # ignore this object and its children
            pass
        else:
            for value in obj.values():
                integers.extend(find_numbers(value))
    else:
        # Ignore other types
        pass
    return integers

if __name__ == "__main__":

    tests = [
        ('[1,2,3]', 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6)
    ]
    for test, expected in tests:
        test_json = json.loads(test)
        numbers = find_numbers(test_json)
        sum_numbers = sum(numbers)
        result = "V" if sum_numbers == expected else "F"
        print(f"[{result}] Test: {test} -> sum: {sum_numbers} (expected: {expected})")

    print("-"*50)

    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.read()
    data_json = json.loads(data)

    numbers = find_numbers(data_json)
    sum_numbers = sum(numbers)
    print(f"Sum of all numbers: {sum_numbers}")
