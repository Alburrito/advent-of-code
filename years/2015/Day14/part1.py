import os
from typing import Tuple

NAME_IDX = 0
SPEED_IDX = 3
FLY_TIME_IDX = 6
REST_TIME_IDX = 13

def parse_line(line: str) -> Tuple[str, int, int, int]:
    """
    Parses a line of input and returns the reindeer's name, speed, fly time, and rest time.
    Args:
        line (str): The input line to parse.
    Returns:
        tuple: A tuple containing the reindeer's name, speed, fly time, and rest time.
    """
    words = line.split()
    name = words[NAME_IDX]
    speed = int(words[SPEED_IDX])
    fly_time = int(words[FLY_TIME_IDX])
    rest_time = int(words[REST_TIME_IDX])
    return name, speed, fly_time, rest_time

class Reindeer:
    """Reindeer class"""

    def __init__(self, name: str, speed: int, fly_time: int, rest_time: int):
        """
        Returns an instance of a Reindeer.
        When flying, rest_time_left is 0.
        When resting, fly_time_left is 0.
        Attributes:
            name (str): The name of the reindeer.
            speed (int): The speed of the reindeer.
            fly_time (int): The time the reindeer can fly.
            rest_time (int): The time the reindeer must rest.
            fly_time_left (int): The time left for the reindeer to fly.
            rest_time_left (int): The time left for the reindeer to rest.
            distance (int): The distance traveled by the reindeer.
        """
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.fly_time_left = self.fly_time
        self.rest_time = rest_time
        self.rest_time_left = 0
        self.distance = 0

    def act(self):
        """
        Each second, the reindeer acts, either flying or resting
        """
        # Check if the reindeer is flying
        if self.fly_time_left > 0:
            # Advance
            self.fly_time_left -= 1
            self.distance += self.speed
            # If no more fly time left, rest time starts
            if self.fly_time_left == 0:
                self.rest_time_left = self.rest_time
        # Check if the reindeer is resting
        elif self.rest_time_left > 0:
            # Rest (no advance)
            self.rest_time_left -= 1
            # If no more rest time left, fly time starts
            if self.rest_time_left == 0:
                self.fly_time_left = self.fly_time


if __name__ == "__main__":

    print("TEST:")    
    max_seconds = 1000
    test_data = [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
    ]

    # Create list of reindeers
    reindeers: list[Reindeer] = []
    for line in test_data:
        name, speed, fly_time, rest_time = parse_line(line)
        reindeer = Reindeer(name, speed, fly_time, rest_time)
        reindeers.append(reindeer)
    
    # Race
    for _ in range(max_seconds):
        for reindeer in reindeers:
            reindeer.act()
    
    # Sort reindeers by distance
    reindeer_distances = {
        reindeer.name: reindeer.distance
        for reindeer in reindeers
    }
    reindeer_distances = dict(
        sorted(reindeer_distances.items(), key=lambda item: item[1], reverse=True)
    )

    # Print results
    for name, distance in reindeer_distances.items():
        print(f"Reindeer {name} traveled {distance} km in {max_seconds}s")


    print("-"*50)

    print("SOLUTION:")
    max_seconds = 2503
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(directory, 'input'), 'r') as f:
        data = f.readlines()
    
    # Create list of reindeers
    reindeers: list[Reindeer] = []
    for line in data:
        name, speed, fly_time, rest_time = parse_line(line)
        reindeer = Reindeer(name, speed, fly_time, rest_time)
        reindeers.append(reindeer)

    # Race
    for _ in range(max_seconds):
        for reindeer in reindeers:
            reindeer.act()
    
    # Sort reindeers by distance
    reindeer_distances = {
        reindeer.name: reindeer.distance
        for reindeer in reindeers
    }
    reindeer_distances = dict(
        sorted(reindeer_distances.items(), key=lambda item: item[1], reverse=True)
    )

    # Print results
    for name, distance in reindeer_distances.items():
        print(f"Reindeer {name} traveled {distance} km in {max_seconds}s")
