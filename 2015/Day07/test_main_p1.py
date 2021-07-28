with open('input', 'r') as f:
    data = f.readlines()


def load(value, wire, wire_dir):
    wire_dir[wire] = value

def operation(operator, op1, op2, wire, wire_dir):
    if operator == 'AND':
        try:
            w1 = wire_dir[op1]
        except:
            w1 = 0
        try:
            w2 = wire_dir[op2]
        except:
            w2 = 0
        wire_dir[wire] = w1 & w2
    if operator == 'OR':
        try:
            w1 = wire_dir[op1]
        except:
            w1 = 0
        try:
            w2 = wire_dir[op2]
        except:
            w2 = 0
        wire_dir[wire] = w1 | w2
    if operator == 'LSHIFT':
        try:
            w1 = wire_dir[op1]
        except:
            w1 = 0
        shifts = int(op2)
        wire_dir[wire] = w1 << shifts
    if operator == 'RSHIFT':
        try:
            w1 = wire_dir[op1]
        except:
            w1 = 0
        shifts = int(op2)
        wire_dir[wire] = w1 >> shifts



wire_dir = {}
for instruction in data:
    instruction = instruction.replace('\n', '')
    print(instruction)
    splitted = instruction.split(" ")
    if splitted[0].isdigit(): # Load
        value = int(splitted[0])
        wire = splitted[2]
        load(value, wire, wire_dir)
    else:
        if splitted[0] == 'NOT':
            value = int(wire_dir[splitted[1]]) ^ 0xffff
            wire = splitted[3]
            load(value, wire, wire_dir)
        else: # Any other operation
            op1 = splitted[0]
            op2 = splitted[2]
            operator = splitted[1]
            wire = splitted[4]
            operation(operator, op1, op2, wire, wire_dir)

    print(wire_dir)
    print("------")

print("")

for key in wire_dir:
    print(f'{key} -> {wire_dir[key]}')