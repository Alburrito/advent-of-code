from hashlib import md5

## Part One ##
secret = "ckczppom"
i = 0

def starts_with_five_zeroes(hash):
    return hash[:5] == "00000"

while True:
    if i % 10000 == 0:
        print(i)

    combination = secret + str(i)  
    hash = md5(combination.encode()).hexdigest()
    if starts_with_five_zeroes(hash):
        print(f'Hash: {hash}\n')
        print(f'Combination: {combination}')
        print(f'Number: {i}')
        break
    i += 1


print('------------------------------------------')


## Part Two ##
i = 0

def starts_with_six_zeroes(hash):
    return hash[:6] == "000000"

while True:
    if i % 10000 == 0:
        print(i)

    combination = secret + str(i)  
    hash = md5(combination.encode()).hexdigest()
    if starts_with_six_zeroes(hash):
        print(f'Hash: {hash}\n')
        print(f'Combination: {combination}')
        print(f'Number: {i}')
        break
    i += 1
