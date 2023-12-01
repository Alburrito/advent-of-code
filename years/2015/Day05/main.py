with open('input', 'r') as f:
    data = f.readlines()


## Part One ## 

def has_min_three_vowels(string):
    return len([c for c in string if c in 'aeiou']) >= 3

def has_min_one_repeated_letter(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def contains_forbidden_string(string):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for f in forbidden:
        if f in string:
            return True
    return False

nice_strings = 0 

for string in data:
    if not contains_forbidden_string(string):
        if has_min_three_vowels(string):
            if has_min_one_repeated_letter(string):
                nice_strings += 1

print(f'Nice strings (Part one): {nice_strings}')


## Part Two ##

def has_a_pair_of_letters_twice_without_overlapping(string):
    for i in range(len(string) - 2):
        pair = string[i:i+2]
        for j in range(i+2, len(string) - 1):
            new_pair = string[j:j+2]
            if pair == new_pair:
                return True
    return False

def repeats_with_one_letter_in_between(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

nice_strings = 0 


for string in data:
    if has_a_pair_of_letters_twice_without_overlapping(string):
        if repeats_with_one_letter_in_between(string):
            nice_strings += 1

print(f'Nice strings (Part two): {nice_strings}')
