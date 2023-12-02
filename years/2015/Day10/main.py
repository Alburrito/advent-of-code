# COMPLETED

COLUMN_WIDTH = 10

def look_and_say(number):
    digits = list(number)
    new_number = ""

    idx = 0
    while idx < len(digits):
        digit = digits[idx]
        copies = 1
        finished = False

        # Last digit with no comparision
        if idx == len(digits)-1:
            new_number += f"{copies}{digit}"
            finished = True
            break

        idx_step = 1

        while ( # Compare with next digit
            digits[idx + idx_step] == digit # Next digit is the same
        ):
            copies += 1
            idx_step += 1
            # Break if no more digits to compare
            if idx + idx_step == len(digits):
                finished = True
                break

        new_number += f"{copies}{digit}"
        if finished:
            break
        idx += idx_step

    return new_number

if __name__ == "__main__":

    with open("input", "r") as f:
        input_number = f.read().strip()

    numbers = ["1","11","21","1211","111221"]
    print("Test numbers:")
    for number in numbers:
        print(f"{number}: ".ljust(COLUMN_WIDTH), look_and_say(number))

    print()

    number = input_number
    for i in range(50):
        number = look_and_say(number)
        if i == 39:
            print(f"Lenght after {i+1} processes: {len(number)}")
    print(f"Lenght after {i+1} processes: {len(number)}")
