# COMPLETED

import os
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <1|2>")
        sys.exit(1)
    option = sys.argv[1]
    day_dir = os.path.dirname(os.path.abspath(__file__))

    if option == "1":
        subprocess.run(["python3", os.path.join(day_dir, "part1.py")])
    elif option == "2":
        subprocess.run(["python3", os.path.join(day_dir, "part2.py")])
    else:
        print("Invalid option. Use '1' to run part1.py or '2' to run part2.py.")
        sys.exit(1)

if __name__ == "__main__":
    main()
