# COMPLETED

import os
from itertools import combinations
from typing import List, Tuple

def solve(total_liters: int, containers: List[int]) -> List[Tuple[int,...]]:
    """
    Finds the combinations of containers that sum up to the given total liters
    using the minimum number of containers.

    Args:
        total_liters (int): The target amount of liters to be stored.
        containers (List[int]): A list of integers representing the capacities of the containers.

    Returns:
        List[Tuple[int, ...]]: A list of tuples, where each tuple represents a combination
        of container capacities.
    """
    comb_containers = []
    for i in range(len(containers)):
        comb_containers.extend([
            combo
            for combo in combinations(containers, i)
            if sum(combo) == total_liters
        ])
        if comb_containers:
            break
    return comb_containers

if __name__ == "__main__":
    
    print("TEST:")
    containers = [
        20, 15, 10, 5, 5
    ]

    comb_containers = solve(25, containers)    
    print(len(comb_containers))

    print("-"*50)

    print("SOLUTION:")
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.readlines()

    containers = [
        int(container)
        for container in data
    ]
    comb_containers = solve(150, containers)
    print(len(comb_containers))

