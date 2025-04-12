# COMPLETED

import os
import re
from typing import Dict, Tuple

def parse_line(line: str) -> Tuple[int, Dict[str, int]]:
    """
    Parses a line of text describing a Sue and her compounds.

    The line must follow the format:
    "Sue <number>: <compound1>: <value1>, <compound2>: <value2>, ..."

    Args:
        line (str): A line of text describing a Sue.

    Returns:
        Tuple[int, Dict[str, int]]: A tuple containing:
            - The Sue's number (int).
            - A dictionary with the compounds and their values (Dict[str, int]).

    Raises:
        ValueError: If the line does not match the expected format.
    """
    pattern = r"Sue (\d+): (.+)"
    match = re.search(pattern, line)
    if not match:
        raise ValueError('Wrong Sue format')

    n_sue = int(match.group(1))
    compounds_match = match.group(2)
    
    pattern = r"(\w+): (\d+),?\s?"
    match = re.findall(pattern, compounds_match)
    compounds = {}
    for compound in match:
        compounds[compound[0]] = int(compound[1])
    
    return n_sue, compounds


if __name__ == "__main__":

    TICKER_TAPE = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.readlines()
    
    for line in data:
        valid = True
        n_sue, compounds = parse_line(line)
        for compound, value in compounds.items():
            if compound in ('cats', 'trees'):
                if TICKER_TAPE[compound] >= value:
                    valid = False
                    break
            elif compound in ('pomeranians', 'goldfish'):
                if TICKER_TAPE[compound] <= value:
                    valid = False
                    break
            else:
                if TICKER_TAPE[compound] != value:
                    valid = False
                    break

        if valid:
            print(n_sue, compounds)
            break
