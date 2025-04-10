# This file contains utility functions for the Advent of Code repository.
# This IS NOT RELATED with the Advent of Code challenge itself.
# It is only used to easily run challenges from root folder.

# If you still want to use this file, you can do it by running:
# python3 main.py YYYY DD N
# where:
# - YYYY is the year of the challenge (e.g., 2015)
# - DD is the day of the challenge (e.g., 13 or 02)
# - N is the part of the challenge (1 or 2)

import os
import sys

def run_part(year: str, day: str, part: str):
    """
    Executes the specified part of the Advent of Code challenge.

    Args:
        year (str): The year of the challenge (e.g., "2015").
        day (str): The day of the challenge (e.g., "13 or 02").
        part (str): The part of the challenge (e.g., "1" or "2").

    Raises:
        FileNotFoundError: If the specified day or part does not exist.
    """
    # Construct the path to the script
    script_path = os.path.join("years", year, f"Day{day.zfill(2)}", f"part{part}.py")

    # Check if the script exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script for year {year}, day {day}, part {part} does not exist.")

    # Execute the script
    os.system(f"python3 {script_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py YYYY DD N")
        print("  YYYY: Year of the challenge (e.g., 2015)")
        print("  DD: Day of the challenge (e.g., 13 or 02)")
        print("  N: Part of the challenge (1 or 2)")
        sys.exit(1)

    year, day, part = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        run_part(year, day, part)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
