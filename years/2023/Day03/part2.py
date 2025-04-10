# COMPLETED

import os
import re

def contains_symbol(string, symbols):
    """
    If symbol found, return [{
        'symbol': symbol,
        'position': position
    }...]
    """
    found_symbols = []
    for pos, char in enumerate(string):
        if char in symbols:
            found_symbols.append({
                'symbol': char,
                'position': pos
            })
    return found_symbols

def get_number_indexes(string):
    """
    For every number found, return [{
        'number': number,
        'start_idx': start_idx,
        'end_idx': end_idx
    }]
    """
    number_indexes = []
    for match in re.finditer(r'\d+', string):
        number_indexes.append({
            'number': int(match.group()),
            'start_idx': match.start(),
            'end_idx': match.end() - 1  # Adjust end index to match the last digit of the number
        })
    return number_indexes

def get_numbers_around(data, sym_row, sym_col):
    """
    For the current, the last and the next row, get the numbers and their indexes
    Check if the symbol is in the range of the number
    If so, add the number to the list
    """
    numbers = []
    current_row = data[sym_row]
    last_row = data[sym_row -1] if sym_row > 0 else None
    next_row = data[sym_row +1] if sym_row < len(data) - 1 else None

    # Current row
    current_row_number_idx = get_number_indexes(current_row)
    for number in current_row_number_idx:
        if any([
            number['end_idx'] == sym_col-1, # ...N*s...
            number['start_idx'] == sym_col+1, # ...s*N...
        ]):
            numbers.append(number['number'])
    
    # Last row
    if last_row:
        last_row_number_idx = get_number_indexes(last_row)
        for number in last_row_number_idx:
            # Iterate over the 3 columns around the symbol
            # If any of them is in the range of the number, add it to the list
            for i in range(-1, 2): # -1, 0, 1
                if number['start_idx'] <= sym_col+i <= number['end_idx']:
                    numbers.append(number['number'])
                    break
    
    # Next row
    if next_row:
        next_row_number_idx = get_number_indexes(next_row)
        for number in next_row_number_idx:
            # Iterate over the 3 columns around the symbol
            # If any of them is in the range of the number, add it to the list
            for i in range(-1, 2):
                if number['start_idx'] <= sym_col+i <= number['end_idx']:
                    numbers.append(number['number'])
                    break
            
    return numbers

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.read().splitlines()


    samples = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]
    
    # Search possible symbols
    symbols = []
    for row, item in enumerate(data):
        # Search for symbols, not .
        for char in item:
            if not char.isdigit() and char != '.':
                symbols.append(char)
    symbols = list(set(symbols))
    print(f"Symbols: {symbols}")

    print("Part One:")
    numbers = []
    for row_idx, row in enumerate(samples):
        symbols_found = contains_symbol(row, symbols)
        if symbols_found:
            for symbol in symbols_found:
                numbers_around = get_numbers_around(samples, row_idx, symbol['position'])
                numbers.extend(numbers_around)
    print("SAMPLES:")
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")

    print("-"*15)
    numbers = []
    for row_idx, row in enumerate(data):
        symbols_found = contains_symbol(row, symbols)
        if symbols_found:
            for symbol in symbols_found:
                numbers_around = get_numbers_around(data, row_idx, symbol['position'])
                numbers.extend(numbers_around)
    print("INPUT:")
    print(f"Sum: {sum(numbers)}")

    print("-"*30)
    print("Part Two:")
    gear_ratios = []
    symbols = ["*"]
    for row_idx, row in enumerate(samples):
        symbols_found = contains_symbol(row, symbols)
        if symbols_found:
            for symbol in symbols_found:
                gears_around = get_numbers_around(samples, row_idx, symbol['position'])
                if len(gears_around) == 2:
                    gear_ratio = gears_around[0]*gears_around[1]
                    gear_ratios.append(gear_ratio)
    print("SAMPLES:")
    print(f"Numbers: {gear_ratios}")
    print(f"Sum: {sum(gear_ratios)}")

    print("-"*15)
    gear_ratios = []
    symbols = ["*"]
    for row_idx, row in enumerate(data):
        symbols_found = contains_symbol(row, symbols)
        if symbols_found:
            for symbol in symbols_found:
                gears_around = get_numbers_around(data, row_idx, symbol['position'])
                if len(gears_around) == 2:
                    gear_ratio = gears_around[0]*gears_around[1]
                    gear_ratios.append(gear_ratio)
    print("INPUT:")
    print(f"Sum: {sum(gear_ratios)}")
