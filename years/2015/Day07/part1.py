# COMPLETED

import os

NUM_BITS = 16

def parse_line(line: str):
    input_a = None
    input_b = None
    output = None
    operator = None
    line = line.split()
    if len(line) == 3:
        # Assign
        input_a = line[0]
        operator = "ASSIGN"
        output = line[2]
    elif len(line) == 4:
        # NOT
        input_a = line[1]
        operator = "NOT"
        output = line[3]
    elif len(line) == 5:
        # AND, OR, LSHIFT, RSHIFT
        input_a = line[0]
        operator = line[1]
        input_b = line[2]
        output = line[4]
    else:
        raise ValueError(f"Invalid line: {line}")
    return input_a, input_b, operator, output

def operate(value_a, value_b, operator):
    if operator == "ASSIGN":
        result = value_a
    elif operator == "NOT":
        result = ~value_a
    elif operator == "AND":
        result = value_a & value_b
    elif operator == "OR":
        result = value_a | value_b
    elif operator == "LSHIFT":
        result = value_a << value_b
    elif operator == "RSHIFT":
        result = value_a >> value_b
    else:
        raise ValueError(f"Invalid operator: {operator}")

    return result & ((1 << NUM_BITS) - 1) # Mask to 16 bits

def all_wires_solved(wires: dict, wires_set: set):
    for wire in wires_set:
        if wire not in wires:
            return False
    return True

if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), 'input_2'), 'r') as file:
        instructions = file.read().splitlines()
    n_instructions = len(instructions)

    # Create wire set to check if all wires are solved
    wires_set = set()
    for instruction in instructions:
        input_a, input_b, operator, output = parse_line(instruction)
        if input_a.isalpha():
            wires_set.add(input_a)
        if input_b and input_b.isalpha():
            wires_set.add(input_b)
        if output.isalpha():
            wires_set.add(output)
    # Sort wires alphabetically
    wires_set = sorted(wires_set)

    solved_wires = {} # id:value
    pending_instructions = instructions.copy()

    iter = 0
    while not all_wires_solved(solved_wires, wires_set):
        instructions = pending_instructions.copy()
        pending_instructions = []
        for instruction in instructions:
            input_a, input_b, operator, output = parse_line(instruction)
            value_b = None # Default value
            if input_a.isnumeric():
                value_a = int(input_a)
            else: # Wire
                value_a = solved_wires[input_a] if input_a in solved_wires else None
            
            if value_a is None:
                # Skip instruction because a needed wire is not solved yet
                pending_instructions.append(instruction)
                continue
            
            if operator in ["AND", "OR", "LSHIFT", "RSHIFT"]: # Needs second input
                if input_b.isnumeric():
                    value_b = int(input_b)
                else:
                    value_b = solved_wires[input_b] if input_b in solved_wires else None
                
                if value_b is None:
                    # Skip instruction because a needed wire is not solved yet
                    pending_instructions.append(instruction)
                    continue
            
            solved_wires[output] = operate(value_a, value_b, operator)

        iter += 1
        print(f"IT-{iter} - pending instructions: {len(instructions)}/{n_instructions}")
        print(f"IT-{iter} - solved wires: {len(solved_wires)}/{len(wires_set)}")
        print("-"*25)
    
    solved_wires = {k: v for k, v in sorted(solved_wires.items(), key=lambda item: item[0])}
    # print(solved_wires)
    print(f"RESULT - Wire 'a' value: {solved_wires['a']}")




