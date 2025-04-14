# COMPLETED

import os
from typing import List


def get_input_path() -> str:
    """
    Returns the path to the input file.

    Returns:
        str: The absolute path to the input file located in the same directory as this script.
    """
    return os.path.join(os.path.dirname(__file__), 'input')
    

ON = "#"
OFF = "."

class Neighborhood:
    """
    Represents a grid of lights in a neighborhood and simulates their behavior
    based on specific rules for turning lights on and off.
    """

    def __init__(self, data: List[str]):
        """
        Initializes the neighborhood with the given grid of lights.

        Args:
            data (List[str]): A list of strings representing the initial state of the grid.
                              Each string corresponds to a row in the grid, where '#' is ON
                              and '.' is OFF.
        """
        self.neighborhood: List[str] = data

    def print(self):
        """
        Prints the current state of the neighborhood grid to the console.
        """
        for street in self.neighborhood:
            print(street.strip())
    
    def run_lights(self, n_steps: int, verbosity: bool = True):
        """
        Simulates the behavior of the lights for a given number of steps.

        Args:
            n_steps (int): The number of steps to simulate.
            verbosity (bool): If True, prints the state of the grid after each step.
        """
        if verbosity:
            print("Initial state:")
            self.print()
            print("-" * 2 * len(self.neighborhood[0]))
        for step in range(n_steps):
            self._step()
            if verbosity:
                print(f"After {step+1} step:")
                self.print()
                print("-" * 2 * len(self.neighborhood[0]))
    
    def count_lights_on(self) -> int:
        """
        Counts the number of lights that are currently ON in the neighborhood.

        Returns:
            int: The number of lights that are ON.
        """
        lights_on = [
            light
            for street in self.neighborhood
            for light in street
            if light == ON
        ]
        return len(lights_on)

    def _step(self):
        """
        Updates the state of the neighborhood grid by applying the rules to all lights.
        The update is performed simultaneously for all lights.
        """
        new_state: List[str] = []
        for i, street in enumerate(self.neighborhood):
            new_state.append("")
            for j, _ in enumerate(street):
                new_light_state = self._next_light_state(i, j)
                new_state[i] += new_light_state
        self.neighborhood = new_state
                

    def _next_light_state(self, i: int, j: int) -> str:
        """
        Determines the next state of a light at a given position based on its current state
        and the number of ON neighbors.

        Args:
            i (int): The row index of the light.
            j (int): The column index of the light.

        Returns:
            str: The next state of the light ('#' for ON, '.' for OFF).
        """
        on_neighbors = self._on_neighbors(i, j)
        if self.neighborhood[i][j] == ON:
            if on_neighbors in (2,3):
                return ON
            else:
                return OFF
        else:
            if on_neighbors == 3:
                return ON
            else:
                return OFF
    
    def _on_neighbors(self, x: int, y: int) -> int:
        """
        Counts the number of ON neighbors for a light at a given position.

        Args:
            x (int): The row index of the light.
            y (int): The column index of the light.

        Returns:
            int: The number of neighbors that are ON.
        """
        on_neighbors = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    continue
                if i < 0 or len(self.neighborhood) <= i:
                    continue
                if j < 0 or len(self.neighborhood[i]) <= j:
                    continue
                if self.neighborhood[i][j] == OFF:
                    continue
                on_neighbors += 1

        return on_neighbors
    

if __name__ == "__main__":
    
    print("TEST:")
    data = [
        ".#.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####.."
    ]

    neighborhood = Neighborhood(data)
    n_steps = 4
    neighborhood.run_lights(n_steps, True)
    print(f"After {n_steps} steps, there are {neighborhood.count_lights_on()} lights on")

    print("-" * 50)

    print("SOLUTION:")
    with open(get_input_path(), 'r') as f:
        data = [line.strip() for line in f.readlines()]
    
    neighborhood = Neighborhood(data)
    n_steps = 100
    neighborhood.run_lights(n_steps)
    print(f"After {n_steps} steps, there are {neighborhood.count_lights_on()} lights on")