

class Gate():

    def __init__(self, input_wires: list, output_wire: str):
        self.input_wires = input_wires
        self.output_wire = output_wire
        self.input_gate = None
        self.output_gate = []
        self.type = None

    def evaluate(self):
        pass

    def __str__(self):
        msg = f"Gate {self.type}: "
        [msg += f"{i} " for i in self.input_wires]
        msg += f"-> {self.output_wire}"
        # msg += f"\n\tInput: {self.input_gate}"
        # msg += f"\n\tOutput: {self.output_gate}"
        msg += f"\n--------------------------------------------------------"
        return  msg

class LOAD_Gate(Gate):
    def __init__(self, input_wires, output_wire):
        super().__init__(input_wires, output_wire)
        self.type = "LOAD"
    
    def evaluate(self,db):
        db[self.output_wire] = int(self.input_wires[0])
        [gate.evaluate() for gate in self.output_gate]


class NOT_Gate(Gate):
    def __init__(self, input_wires, output_wire):
        super().__init__(input_wires, output_wire)
        self.type = "NOT"

    def evaluate(self, db):
        if self.input_wires[0] in db:
            db[self.output_wire] = ~ db[self.input_wires[0]]
            [gate.evaluate() for gate in self.output_gate]
        else:
            pass


class AND_Gate(Gate):
    def __init__(self, input_wires, output_wire):
        super().__init__(input_wires, output_wire)
        self.type = "AND"

    def evaluate(self,db):
        if self.input_wires[0] in db and self.input_wires[1] in db:
            input_1 = db[self.input_wires[0]]
            input_2 = db[self.input_wires[1]]
            db[self.output_wire] =  input_1 & input_2
            [gate.evaluate() for gate in self.output_gate]


class OR_Gate(Gate):
    def __init__(self, input_wires, output_wire):
        super().__init__(input_wires, output_wire)
        self.type = "OR"

    def evaluate(self,db):
        input_1 = db[self.input_wires[0]]
        input_2 = db[self.input_wires[1]]
        db[self.output_wire] = input_1 | input_2
        [gate.evaluate() for gate in self.output_gate]


class LSHIFT_Gate(Gate):
    def __init__(self, input_wires, output_wire):
        super().__init__(input_wires, output_wire)
        self.type = "LSHIFT"

    def evaluate(self,db):
        input_1 = db[self.input_wires[0]]
        shift = self.input_wires[1]
        db[self.output_wire] = input_1 << shift
        [gate.evaluate() for gate in self.output_gate]

class RSHIFT_Gate(Gate):
    def __init__(self, input_wires, output_wire):
        super().__init__(input_wires, output_wire)
        self.type = "RSHIFT"

    def evaluate(self,db):
        input_1 = db[self.input_wires[0]]
        shift = self.input_wires[1]
        db[self.output_wire] = input_1 >> shift
        [gate.evaluate() for gate in self.output_gate]


class Circuit():

    def __init__(self, inputpath):
        with open(inputpath, 'r') as f:
            self.data = f.readlines()

        self.gates = []
        self.db = {}

    def search_gates(self, gate):
        for g in self.gates:
            if g.input_wires == gate.output_wire:
                gate.output_gate.append(g)
                g.input_gate = gate


    def create_circuit(self):
        print('Loading gates...')
        for line in self.data:
            line = line.split()
            print(line)
            if line[0] == 'NOT':
                self.gates.append(NOT_Gate(line[1], line[3]))
            elif line[0].isdigit():
                self.gates.append(LOAD_Gate(int(line[0]), line[2]))
            else:
                if line[1] == 'AND':
                    self.gates.append(AND_Gate([line[0], line[2]], line[4]))
                elif line[1] == 'OR':
                    self.gates.append(OR_Gate([line[0], line[2]], line[4]))
                elif line[1] == 'LSHIFT':
                    self.gates.append(LSHIFT_Gate([line[0], line[2]], line[4]))
                elif line[1] == 'RSHIFT':
                    self.gates.append(RSHIFT_Gate([line[0], line[2]], line[4]))
        
        print('Loaded gates.')

        print('Connecting gates...')
        for gate in self.gates:
            self.search_gates(gate)
        print('Connected gates.')

    def evaluate(self):
        print('Evaluating...')
        for gate in self.gates:
            print(self.db)
            print(gate)
            if gate.type == 'LOAD':
                gate.evaluate(self.db)
        print('Evaluated.')


c = Circuit('input')
c.create_circuit()
c.evaluate()
print(c.db)


print("")
print("")
print("")

for g in c.gates:
    print(g)
    print("")