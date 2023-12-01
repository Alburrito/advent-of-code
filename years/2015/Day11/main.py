# Must be 8 characters long
# Increment until is valid
# Increment: xx -> xy -> xz -> ya -> yb...
# At least three straight increasing letters abc, bcd, cde, ...
# No i, o or l
# Non overlapping pairs of letters aa, bb, cc, ...

PASSWORD_LENGTH = 8
FORBIDDEN_CHARS = ["i", "o", "l"]

# Using unicode, we can check for increasing letters

def is_valid(password):
    # Check length
    if len(password) != PASSWORD_LENGTH:
        return False

    # Check for forbidden letters
    if any(c in password for c in FORBIDDEN_CHARS):
        return False

    # Check for three increasing letters
    for i in range(len(password) - 2):
        if all([
            ord(password[i]) == ord(password[i + 1]) - 1, # unicode i = unicode i+1
            ord(password[i]) == ord(password[i + 2]) - 2  # unicode i = unicode i+2
        ]):
            break
    else: # If the loop didn't break, we didn't find three increasing letters
        return False

    # Check for the two different pairs
    pairs = set()
    for i in range(len(password) - 1):
        if all([
            password[i] not in pairs, # If we already found a pair with this char, skip
            password[i] == password[i + 1] # If the next char is the same, we found a pair
        ]):
            pairs.add(password[i])
    if len(pairs) < 2:
        return False

    return True

def increment_password(password):
    """
    Recursive function.
    Increments password by one. If last character is z, increment the previous characters
    and append a.
    inc(azz) -> inc(az)+a -> inc(a)+a+a -> baa
    """
    new_password = increment_password(password[:-1]) + "a" \
        if password[-1] == "z" else \
        password[:-1] + chr(ord(password[-1]) + 1)

    return new_password

def increment_until_valid(password, solution):
    """
    Increments password until it is valid
    """
    print(f"Password {password} should increment to {solution if solution else 'something valid'}")
    print("Incrementing until valid password...")

    iterations = 1
    new_password = increment_password(password)
    while not is_valid(new_password):
        iterations += 1
        new_password = increment_password(new_password)

    print(f"Found a valid password. Iterations: {iterations}")
    print(f"Password {password} increments to {new_password}")
    if solution:
        print(f"{'CORRECT' if new_password == solution else 'WRONG'}")
    return new_password, iterations

if __name__ == "__main__":

    with open("input") as f:
        input_password = f.read().strip()

    test_passwords = [
        "hijklmmn", "abbceffg", "abbcegjk", "abcdefgh",
        "abcdffaa", "ghijklmn", "ghjaabcc",
        "abcdefgg"
    ]
    for pw in test_passwords:
        print(
            f"Password {pw} " \
            f"{'is' if is_valid(pw) else 'is not'} valid"
        )
    
    print("-" * 20)
    print("Test incrementing")
    password = "abcdefgh"
    solution = "abcdffaa"
    new_password, iterations = increment_until_valid(password, solution)

    print("-" * 20)
    password = "ghijklmn"
    solution = "ghjaabcc"
    new_password, iterations = increment_until_valid(password, solution)

    print("-" * 20)
    print("PART ONE: Incrementing input password")
    new_password, iterations = increment_until_valid(input_password, None)

    print("-" * 20)
    print("PART TWO: Incrementing new password")
    new_password, iterations = increment_until_valid(new_password, None)
