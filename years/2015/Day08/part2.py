# COMPLETED

import os
import re

def decode(string):
    """
    Returns a string with all the escaped characters replaced by a single one.
    Alphabetic letters are easier to code with than escaped characters :)
    They can be printed without losing your mind (but only for Santa problems)
    """
    # Remove first and last "
    string = string[1:-1]
    # Replace escaped backslash with ONE character
    string = re.sub(r'\\\\', 'B', string)
    # Replace escaped double quote with ONE character
    string = re.sub(r'\\"', 'Q', string)
    # Replace hex sequences with ONE character
    string = re.sub(r'\\x[0-9a-f]{2}', 'H', string)
    return string

def encode(string):
    """
    Returns the string replacing the must-be-escaped characters with some letters
    Adds first and last "
    """
    # Replace double quote with encoded double quote " -> \"
    string = re.sub(r'\"', 'BQ', string)
    # Replace backslash with enconded backslash \ -> \\
    string = re.sub(r'\\', 'BB', string)
    # Add first and last "
    string = f'"{string}"'
    return string

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        strings = f.readlines()
    
    n_str_literals = 0
    n_str_mem_values = 0
    n_encoded_str_literals = 0
    
    for string in strings:
        # Every string except last one has a \n at the end
        mod_string = string[:-1] if string[-1] == '\n' else string

        n_str_literals += len(mod_string)
        n_str_mem_values += len(decode(mod_string))
        n_encoded_str_literals += len(encode(mod_string))

    column_width = 31
    print("PART ONE:")
    print('Num of string literals:'.ljust(column_width), n_str_literals)
    print('Num of string memory values:'.ljust(column_width), n_str_mem_values)
    print('Difference:'.ljust(column_width), n_str_literals - n_str_mem_values)
    print()
    print("PART TWO:")
    print('Num of encoded string literals:'.ljust(column_width), n_encoded_str_literals)
    print('Num of string literals:'.ljust(column_width), n_str_literals)
    print('Difference:'.ljust(column_width), n_encoded_str_literals - n_str_literals)
    print()
    print("EXAMPLE:")
    print('Original string:'.ljust(column_width), strings[0][:-1])
    print('Decoded string:'.ljust(column_width), decode(strings[0][:-1]))
    print('Encoded string:'.ljust(column_width), encode(strings[0][:-1]))
    