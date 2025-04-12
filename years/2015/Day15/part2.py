# COMPLETED


import os
from typing import Dict, List, Sequence, Tuple
from itertools import product

def parse_data(data: List[str]) -> Dict[str, Dict[str, int]]:
    """
    Parses the input data to extract ingredient properties.

    Args:
        data (List[str]): A list of strings, where each string represents an ingredient
                          and its properties in the format:
                          "Ingredient: property1 value1, property2 value2, ...".

    Returns:
        Dict[str, Dict[str, int]]: A dictionary where the keys are ingredient names,
                                   and the values are dictionaries of their properties
                                   (e.g., capacity, durability, flavor, texture, calories).
    """
    ingredients = {}
    for line in data:
        fields = line.split(": ")
        name = fields[0]
        properties = fields[1].split(", ")
        ingredients[name] = {
            'capacity': int(properties[0].split(" ")[1]),
            'durability': int(properties[1].split(" ")[1]),
            'flavor': int(properties[2].split(" ")[1]),
            'texture': int(properties[3].split(" ")[1]),
            'calories': int(properties[4].split(" ")[1])
        }
    return ingredients

def find_teaspoons_combinations(max_teaspoons: int, num_ingredients: int) -> List[Tuple[int, ...]]:
    """
    Finds all possible combinations of teaspoons for a given number of ingredients
    such that the total number of teaspoons equals max_teaspoons.

    Args:
        max_teaspoons (int): The total number of teaspoons to distribute.
        num_ingredients (int): The number of ingredients to distribute teaspoons among.

    Returns:
        List[Tuple[int]]: A list of tuples, where each tuple represents a valid combination
                          of teaspoons for the ingredients.
    """
    numbers = range(0, max_teaspoons + 1)

    return [
        combination for combination in product(numbers, repeat=num_ingredients)
        if sum(combination) == max_teaspoons
    ]

def calculate_property_score(
        property: str, combination: Tuple[int, ...], ingredients: Dict[str, Dict[str, int]]
) -> int:
    """
    Calculates the total score for a specific property based on a combination of teaspoons.

    Args:
        property (str): The property to calculate the score for (e.g., 'capacity', 'durability').
        combination (Tuple[int]): A tuple representing the number of teaspoons assigned to each ingredient.
        ingredients (Dict[str, Dict[str, int]]): A dictionary of ingredients and their properties.

    Returns:
        int: The total score for the specified property.

    Raises:
        ValueError:
            - If the calculated score is less than or equal to 0.
    """
    score = sum([
        ingredients[ingredient][property] * n_teaspoons
        for ingredient, n_teaspoons in zip(ingredients, combination)
    ])
    if score <= 0:
        raise ValueError('Negative or 0 score')
    return score

def calculate_combinations_score(
        combinations: Sequence[Tuple[int, ...]],
        ingredients: Dict[str, Dict[str, int]]
) -> Dict[Tuple[int], int]:
    """
    Calculates the total score for each combination of teaspoons based on ingredient properties.

    Args:
        combinations (List[Tuple[int]]): A list of combinations of teaspoons for the ingredients.
        ingredients (Dict[str, Dict[str, int]]): A dictionary of ingredients and their properties.

    Returns:
        Dict[Tuple[int], int]: A dictionary where the keys are combinations of teaspoons,
                               and the values are the total scores for those combinations.
    """
    combinations_score = {}
    for combination in combinations:
        try: 
            calories = calculate_property_score('calories', combination, ingredients)
            if calories != 500:
                raise ValueError('Calories are not 500')
            capacity = calculate_property_score('capacity', combination, ingredients)
            durability = calculate_property_score('durability', combination, ingredients)
            flavor = calculate_property_score('flavor', combination, ingredients)
            texture = calculate_property_score('texture', combination, ingredients)
            score = capacity * durability * flavor * texture
        except ValueError:
            score = 0
        finally:
            combinations_score[combination] = score
            continue

    return combinations_score

def solve(data: List[str], max_teaspoons: int) -> None:
    """
    Solution to challenge

    Args:
        data (List[str]): A list of strings representing the ingredients and their properties.
        max_teaspoons (int): The total number of teaspoons to distribute among the ingredients.
    """
    ingredients = parse_data(data)
    n_teaspoons_combinations = find_teaspoons_combinations(max_teaspoons, len(ingredients))

    combinations_score = calculate_combinations_score(n_teaspoons_combinations, ingredients)
    sorted_combinations_score = dict(
        sorted(
            # Asceding so the last ones (the ones we see in the terminal) are shown when finished
            combinations_score.items(), key=lambda item: item[1]
        )
    )

    for combination, score in sorted_combinations_score.items():
        print(f"Score {score}:")
        for n_teaspoons, ingredient in zip(combination, ingredients):
            print(f"- {n_teaspoons} teaspoons of {ingredient}.")
        print("-" * 50)


if __name__ == "__main__":
    test_data = [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
    ]

    print("TEST CASE:")
    solve(test_data, 100)

    print("#"*100)

    print("SOLUTION:")
    with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
        data = f.readlines()
    solve(data, 100)
