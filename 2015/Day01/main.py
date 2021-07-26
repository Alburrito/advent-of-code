with open('Day01/input', 'r') as f:
    data = f.read()


def get_floor_and_position(data):
    floor = 0
    position = -1
    for index, char in enumerate(data):
        if char == '(':
            floor += 1
        else:
            floor -= 1

        if position < 0 and floor < 0:
            position = index
            
    return floor, position+1


print(get_floor_and_position(data))

