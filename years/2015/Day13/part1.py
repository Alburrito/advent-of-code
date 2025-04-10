import os
from typing import List, Tuple
from itertools import permutations

PERSON_IDX = 0
ACTION_IDX = 2
QTY_IDX = 3
PARTNER_IDX = -1

def parse_line(line: str) -> Tuple:
    """
    Parses a single line of input data and extracts the person, happiness quantity, 
    and their partner.

    Args:
        line (str): A string describing the happiness change, e.g.,
                    "Alice would lose 79 happiness units by sitting next to Carol."

    Returns:
        tuple: A tuple containing:
            - person (str): The name of the person.
            - qty (int): The happiness change (positive or negative).
            - partner (str): The name of the partner.
    """
    words = line.split(' ')
    person = words[PERSON_IDX]
    qty = words[QTY_IDX]
    if words[ACTION_IDX] == 'lose':
        qty = "-" + qty
    qty = int(qty)
    partner: str = words[PARTNER_IDX]
    partner = partner.replace('.', '')
    partner = partner.replace('\n', '')

    return person, qty, partner

def parse_data(data: List[str]) -> dict:
    """
    Parses the input data and organizes it into a dictionary mapping each person 
    to their happiness changes with each partner.

    Args:
        data (List[str]): A list of strings, where each string describes the happiness 
                          change between two people.

    Returns:
        dict: A nested dictionary where the keys are person names and the values are 
              dictionaries mapping partners to happiness changes.
    """
    guests_info = {}

    for line in data:
        person, qty, partner = parse_line(line)
        if person not in guests_info:
            guests_info[person] = {}
        guests_info[person][partner] = qty

    return guests_info

def calculate_arrangement_happiness(arrangement: Tuple, guests_info: dict) -> int:
    """
    Calculates the total happiness for a given seating arrangement.

    Args:
        arrangement (tuple): A tuple representing the seating order of the guests.
        guests_info (dict): A dictionary containing happiness changes between guests.

    Returns:
        int: The total happiness for the given arrangement.
    """
    arrangement_happiness = 0

    for idx, guest in enumerate(arrangement):
        left_idx = idx-1
        right_idx = idx+1
        # If first guest in the list, left one is the last one
        if idx == 0:
            left_idx = -1
        # If last guest in the list, right one is the first one
        if idx == len(guests_info) - 1: 
            right_idx = 0
        
        left_guest = arrangement[left_idx]
        right_guest = arrangement[right_idx]

        guest_happiness = guests_info[guest][left_guest] + guests_info[guest][right_guest] 
        arrangement_happiness += guest_happiness
    
    return arrangement_happiness

def calculate_best_arrangement(guests_info: dict) -> Tuple:
    """
    Finds the seating arrangement that maximizes total happiness.

    Args:
        guests_info (dict): A dictionary containing happiness changes between guests.

    Returns:
        tuple: A tuple containing:
            - best_arrangement (tuple): The seating arrangement with the highest happiness.
            - best_happiness (int): The total happiness for the best arrangement.
    """
    arrangements = list(permutations(guests_info.keys()))
    best_arrangement = None
    best_happiness = -9999999

    for arrangement in arrangements:
        happiness = calculate_arrangement_happiness(arrangement, guests_info)

        if happiness > best_happiness:
            best_happiness = happiness
            best_arrangement = arrangement
    
    return best_arrangement, best_happiness

if __name__ == "__main__":

    print("TEST:")
    test_data = [
        "Alice would gain 54 happiness units by sitting next to Bob.",
        "Alice would lose 79 happiness units by sitting next to Carol.",
        "Alice would lose 2 happiness units by sitting next to David.",
        "Bob would gain 83 happiness units by sitting next to Alice.",
        "Bob would lose 7 happiness units by sitting next to Carol.",
        "Bob would lose 63 happiness units by sitting next to David.",
        "Carol would lose 62 happiness units by sitting next to Alice.",
        "Carol would gain 60 happiness units by sitting next to Bob.",
        "Carol would gain 55 happiness units by sitting next to David.",
        "David would gain 46 happiness units by sitting next to Alice.",
        "David would lose 7 happiness units by sitting next to Bob.",
        "David would gain 41 happiness units by sitting next to Carol."
    ]
    test_solution = 330
    test_guests_info = parse_data(test_data)
    arrangement, happiness = calculate_best_arrangement(test_guests_info)
    print(f"Best arrangement: {arrangement}")
    print(f"Total happiness: {happiness}")

    print("-"*50)

    print("SOLUTION:")
    directory = os.path.dirname(os.path.abspath(__file__))
    data = []
    with open(os.path.join(directory, 'input'), 'r') as f:
        for line in f.readlines():
            data.append(line)
    guests_info = parse_data(data)
    arrangement, happiness = calculate_best_arrangement(guests_info)
    print(f"Best arrangement: {arrangement}")
    print(f"Total happiness: {happiness}")
