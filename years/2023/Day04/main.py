# COMPLETED

def parse_card(card):
    card_fields = card.split(':') # "Card 1:", numbers
    card_id = int([x for x in card_fields[0].split(' ') if x != ''][1])

    card_winning, card_mine = card_fields[1].split('|')
    card_winning = [int(x) for x in card_winning.split(' ') if x != '']
    card_mine = [int(x) for x in card_mine.split(' ') if x != '']

    return {
        'id': card_id,
        'winning': card_winning,
        'mine': card_mine
    }

def find_mine_winning(card):
    return [
        number for number in card['mine'] if number in card['winning']
    ]

def get_score(mine_winning):
    score = 0
    for number in mine_winning:
        if score == 0:
            score = 1
        else:
            score *= 2
    return score


if __name__ == '__main__':
    with open('input') as f:
        data = f.read().splitlines()
    
    samples = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]

    print("PART ONE:")
    print("Samples:")
    total_score = 0
    for card in samples:
        parsed_card = parse_card(card)
        mine_winning = find_mine_winning(parsed_card)
        total_score += get_score(mine_winning)
    print(f"Total score: {total_score}")

    print("-"*15)

    print("Input:")
    total_score = 0
    for card in data:
        parsed_card = parse_card(card)
        mine_winning = find_mine_winning(parsed_card)
        total_score += get_score(mine_winning)
    print(f"Total score: {total_score}")

    print("-"*30)
    print("PART TWO:")
    print("Samples:")
    parsed_cards = [parse_card(card) for card in samples]
    cards = {
        card['id']: {
            'winning': card['winning'],
            'mine': card['mine'],
            'mine_winning': find_mine_winning(card),
            'n_copies': 1
        } for card in parsed_cards
    }
    for card_id, card in cards.items():
        copies = len(card['mine_winning'])
        for _ in range(card['n_copies']):
            for i in range(1, copies+1):
                cards[card_id+i]['n_copies'] += 1
    
    total_scratchcards = 0
    for card_id, card in cards.items():
        total_scratchcards += card['n_copies']
    print(f"Total scratchcards: {total_scratchcards}")

    print("-"*15)
    print("Input:")
    parsed_cards = [parse_card(card) for card in data]
    cards = {
        card['id']: {
            'winning': card['winning'],
            'mine': card['mine'],
            'mine_winning': find_mine_winning(card),
            'n_copies': 1
        } for card in parsed_cards
    }
    for card_id, card in cards.items():
        copies = len(card['mine_winning'])
        for _ in range(card['n_copies']):
            for i in range(1, copies+1):
                cards[card_id+i]['n_copies'] += 1
    
    total_scratchcards = 0
    for card_id, card in cards.items():
        total_scratchcards += card['n_copies']
    print(f"Total scratchcards: {total_scratchcards}")
