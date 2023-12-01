NUMBERS_REPRESENTATION = {
    'one': '1one',
    'two': '2two',
    'three': '3three',
    'four': '4four',
    'five': '5five',
    'six': '6six',
    'seven': '7seven',
    'eight': '8eight',
    'nine': '9nine',
}
# This way of representing the numbers is needed for strings like
# eightwothree, in which we would lose letters if replacing by just the number

def find_first_and_last_digit(string):
    """
    Finds the digits on a string and returns the first and last digit as an
    integer. If there is only one digit, it returns the same digit twice.
    Example:
        - '1abc2' -> '12'
        - 'pqr3stu8vwx' -> '18'
        - 'aashdbf2sidf' -> '22'
    """
    digits = [int(x) for x in string if x.isdigit()]
    return int(f"{digits[0]}{digits[-1]}") if len(digits) > 1 else \
            int(f"{digits[0]}{digits[0]}")

def replace_numbers(string):
    """
    Replace ocurrences of numbers in their word representation by the number.
    Checks if the string starts with a number in its word representation and
    replaces it by the number. Then recursively calls itself until there are
    no more characters in the string.
    """
    # BASE CASE
    if len(string) == 0:
        return ''
    
    word_repr, digit_repr = starts_with_number(string)
    # eightwothree -> 8eight,wothree -> 8e + replace_numbers('ightwothree') CASE 1 SAMPLE
    # ightwothree -> ightwo,three -> i + replace_numbers('ghtwothree') CASE 2 SAMPLE
    # ...
    # twothree -> 2two,three -> 2t + replace_numbers('wothree')

    if word_repr != '-1': # CASE 1: Starts with a number
        string = digit_repr + string[len(word_repr):]
        return string[:2] + replace_numbers(string[2:])
    
    # CASE 2: Does not start with a number
    return string[0] + replace_numbers(string[1:])       


def starts_with_number(string):
    """
    Returns the number ('number', 'Nnumber') if the string starts with a number in its word representation.
    Returns ('-1', '-1') otherwise.
    """
    for word_repr, digit_repr in NUMBERS_REPRESENTATION.items():
        if string.startswith(word_repr):
            return (word_repr, digit_repr)
    return ('-1', '-1')

if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.read().splitlines()


    print('Part One: ')
    samples = [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet'
    ]

    numbers = []
    for sample in samples:
        numbers.append(find_first_and_last_digit(sample))
    print('Samples: ')
    print(f'- Numbers: {numbers}')
    print(f'- Sum: {sum(numbers)}')

    numbers = []
    for line in data:
        numbers.append(find_first_and_last_digit(line))    
    print('Input: ')
    print(f'- Sum: {sum(numbers)}')

    print('\nPart Two: ')
    samples = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]
    numbers = []
    for sample in samples:
        replaced = replace_numbers(sample)
        resulting_digit = find_first_and_last_digit(replaced)
        numbers.append(resulting_digit)
    print('Samples: ')
    print(f'- Numbers: {numbers}')
    print(f'- Sum: {sum(numbers)}')

    numbers = []
    for line in data:
        replaced = replace_numbers(line)
        resulting_digit = find_first_and_last_digit(replaced)
        numbers.append(resulting_digit)
    print('Input: ')
    print(f'- Sum: {sum(numbers)}')

