# COMPLETED

import os

MAX_BALLS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def parse_item(data_item):
    fields = data_item.split(':')
    game = fields[0] # 'Game XX'
    subsets = fields[1].split(';') # [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']

    colors = []
    for subset in subsets: # ' 3 blue,  4 red
        subset_colors = {'red': 0, 'green': 0, 'blue': 0}
        balls = [x.strip() for x in subset.split(',')] # ['3 blue', '4 red']
        for amount_color in balls: # '3 blue'
            amount, color = amount_color.split(' ')
            subset_colors[color] = int(amount)
        colors.append(subset_colors) # [...{'red': 4, 'green': 0, 'blue': 3}...]

    return {
        'game': int(game.split(' ')[1]), # Get game ID number
        'subsets': subsets,
        'colors': colors
    }

def get_max_balls_revealed(revealed_colors):
    max_balls = {'red': 0, 'green': 0, 'blue': 0}
    for subset in revealed_colors:
        for color, amount in subset.items():
            max_balls[color] = max(max_balls[color], amount)

    return max_balls

def validate_game(max_balls):
    return all(
        [max_balls[color] <= MAX_BALLS[color] for color in max_balls.keys()]
    )

def get_power(max_balls):
    return max_balls['red'] * max_balls['green'] * max_balls['blue']

if __name__ == '__main__':
    
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.readlines()

    samples = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    ]

    # Part One:
    ## Samples
    valid_games_ids = []
    for item in samples:
        parsed = parse_item(item)
        max_balls = get_max_balls_revealed(parsed['colors'])
        if validate_game(max_balls):
            valid_games_ids.append(parsed['game'])
    print(f"[SAMPLE] Sum of valid games ids: {sum(valid_games_ids)}")

    # Input
    valid_games_ids = []
    for item in data:
        parsed = parse_item(item)
        max_balls = get_max_balls_revealed(parsed['colors'])
        if validate_game(max_balls):
            valid_games_ids.append(parsed['game'])
    print(f"[INPUT] Sum of valid games ids: {sum(valid_games_ids)}")

    # Part Two:
    # Samples
    power_list = []
    for item in samples:
        parsed = parse_item(item)
        max_balls = get_max_balls_revealed(parsed['colors'])
        power = get_power(max_balls)
        power_list.append(power)
    print(f"[SAMPLE] Sum of power: {sum(power_list)}")
    
    # Input
    power_list = []
    for item in data:
        parsed = parse_item(item)
        max_balls = get_max_balls_revealed(parsed['colors'])
        power = get_power(max_balls)
        power_list.append(power)
    print(f"[INPUT] Sum of power: {sum(power_list)}")
