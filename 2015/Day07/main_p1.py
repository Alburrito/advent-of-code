

class Gate():

<<<<<<< HEAD
    def __init__(self, input_wires, output_wire):
=======
    def __init__(self, input_wires: list, output_wire: str):
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce
        self.input_wires = input_wires
        self.output_wire = output_wire
        self.input_gates = []
        self.output_gates = []
        self.type = None
        self.evaluated = False

    def evaluate(self):
        return

    def __str__(self):
<<<<<<< HEAD
        msg = f"\n--------------------------------------------------------\n"
        msg += f"Gate {self.type}: {self.input_wires} -> {self.output_wire}"
        msg += f"\n--------------------------------------------------------\n"
=======
        msg = f"Gate {self.type}: "
        [msg += f"{i} " for i in self.input_wires]
        msg += f"-> {self.output_wire}"
        # msg += f"\n\tInput: {self.input_gate}"
        # msg += f"\n\tOutput: {self.output_gate}"
        msg += f"\n--------------------------------------------------------"
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce
        return  msg

class LOAD_Gate(Gate):
    def __init__(self, input_wires, output_wire):
<<<<<<< HEAD
        if input_wires.isdigit():
            parsed_input_wires = int(input_wires)
        else:
            parsed_input_wires = input_wires
        super().__init__(parsed_input_wires, output_wire)
        self.type = "LOAD"
    
    def evaluate(self,db):
        if self.evaluated:
            return
        if self.input_wires not in db:
            if isinstance(self.input_wires, int):
                db[self.output_wire] = self.input_wires
            else:
                return
        else:
            db[self.output_wire] = db[self.input_wires]
        self.evaluated = True
        print(self, db)
        [gate.evaluate(db) for gate in self.output_gates]
=======
        super().__init__(input_wires, output_wire)
        self.type = "LOAD"
    
    def evaluate(self,db):
        db[self.output_wire] = int(self.input_wires[0])
        [gate.evaluate() for gate in self.output_gate]
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce


class NOT_Gate(Gate):
    def __init__(self, input_wires, output_wire):
<<<<<<< HEAD
        if input_wires.isdigit():
            parsed_input_wires = int(input_wires)
        else:
            parsed_input_wires = input_wires
        super().__init__(parsed_input_wires, output_wire)
        self.type = "NOT"

    def evaluate(self, db):
        if self.evaluated:
            return
        if self.input_wires not in db:
            if isinstance(self.input_wires, int):
                db[self.output_wire] = ~ self.input_wires
            else:
                return
        else:
            try:
                db[self.output_wire] = ~ self.input_wires
            except Exception as e:
                print(self, e.with_traceback(e)
                exit()
                
        self.evaluated = True
        print(self, db)
        [gate.evaluate(db) for gate in self.output_gates]
=======
        super().__init__(input_wires, output_wire)
        self.type = "NOT"

    def evaluate(self, db):
        if self.input_wires[0] in db:
            db[self.output_wire] = ~ db[self.input_wires[0]]
            [gate.evaluate() for gate in self.output_gate]
        else:
            pass
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce


class AND_Gate(Gate):
    def __init__(self, input_wires, output_wire):
<<<<<<< HEAD
        parsed_input_wires = []
        for i in input_wires:
            if i.isdigit():
                parsed_input_wires.append(int(i))
            else:
                parsed_input_wires.append(i)
        super().__init__(parsed_input_wires, output_wire)
        self.type = "AND"

    def evaluate(self,db):
        if self.evaluated:
            return
        if self.input_wires[0] not in db:
            if isinstance(self.input_wires[0], int):
                input_1 = self.input_wires[0]
            else:
                return
        else:
            input_1 = db[self.input_wires[0]]

        if self.input_wires[1] not in db:
            if isinstance(self.input_wires[1], int):
                input_2 = self.input_wires[1]
            else:
                return
        else:
            input_2 = db[self.input_wires[1]]
        db[self.output_wire] =  input_1 & input_2
        self.evaluated = True
        print(self, db)
        [gate.evaluate(db) for gate in self.output_gates]
=======
        super().__init__(input_wires, output_wire)
        self.type = "AND"

    def evaluate(self,db):
        if self.input_wires[0] in db and self.input_wires[1] in db:
            input_1 = db[self.input_wires[0]]
            input_2 = db[self.input_wires[1]]
            db[self.output_wire] =  input_1 & input_2
            [gate.evaluate() for gate in self.output_gate]
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce


class OR_Gate(Gate):
    def __init__(self, input_wires, output_wire):
<<<<<<< HEAD
        parsed_input_wires = []
        for i in input_wires:
            if i.isdigit():
                parsed_input_wires.append(int(i))
            else:
                parsed_input_wires.append(i)
        super().__init__(parsed_input_wires, output_wire)
        self.type = "OR"

    def evaluate(self,db):
        if self.evaluated:
            return
        if self.input_wires[0] not in db:
            if isinstance(self.input_wires[0], int):
                input_1 = self.input_wires[0]
            else:
                return
        else:
            input_1 = db[self.input_wires[0]]

        if self.input_wires[1] not in db:
            if isinstance(self.input_wires[1], int):
                input_2 = self.input_wires[1]
            else:
                return
        else:
            input_2 = db[self.input_wires[1]]
=======
        super().__init__(input_wires, output_wire)
        self.type = "OR"

    def evaluate(self,db):
        input_1 = db[self.input_wires[0]]
        input_2 = db[self.input_wires[1]]
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce
        db[self.output_wire] = input_1 | input_2
        self.evaluated = True
        print(self, db)
        [gate.evaluate(db) for gate in self.output_gates]


class LSHIFT_Gate(Gate):
    def __init__(self, input_wires, output_wire):
<<<<<<< HEAD
        parsed_input_wires = []
        for i in input_wires:
            if i.isdigit():
                parsed_input_wires.append(int(i))
            else:
                parsed_input_wires.append(i)
        super().__init__(parsed_input_wires, output_wire)
        self.type = "LSHIFT"

    def evaluate(self,db):
        if self.evaluated:
            return
        if self.input_wires[0] not in db:
            if isinstance(self.input_wires[0], int):
                input_1 = self.input_wires[0]
            else:
                return
        else:
            input_1 = db[self.input_wires[0]]
=======
        super().__init__(input_wires, output_wire)
        self.type = "LSHIFT"

    def evaluate(self,db):
        input_1 = db[self.input_wires[0]]
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce
        shift = self.input_wires[1]
        db[self.output_wire] = input_1 << shift
        self.evaluated = True
        print(self, db)
        [gate.evaluate(db) for gate in self.output_gates]

class RSHIFT_Gate(Gate):
    def __init__(self, input_wires, output_wire):
<<<<<<< HEAD
        parsed_input_wires = []
        for i in input_wires:
            if i.isdigit():
                parsed_input_wires.append(int(i))
            else:
                parsed_input_wires.append(i)
        super().__init__(parsed_input_wires, output_wire)
        self.type = "RSHIFT"

    def evaluate(self,db):
        if self.evaluated:
            return
        if self.input_wires[0] not in db:
            if isinstance(self.input_wires[0], int):
                input_1 = self.input_wires[0]
            else:
                return
        else:
            input_1 = db[self.input_wires[0]]

=======
        super().__init__(input_wires, output_wire)
        self.type = "RSHIFT"

    def evaluate(self,db):
        input_1 = db[self.input_wires[0]]
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce
        shift = self.input_wires[1]
        db[self.output_wire] = input_1 >> shift
        self.evaluated = True
        print(self, db)
        [gate.evaluate(db) for gate in self.output_gates]


class Circuit():

    def __init__(self, inputpath):
        with open(inputpath, 'r') as f:
            self.data = f.readlines()

        self.gates = []
        self.db = {}

    def search_gates(self, gate):
        """
        Para cada puerta:
            Si la salida de la puerta evaluada está en la entrada de la puerta recorrida:
                pe.og.append(p)
                p.ig.append

        bn OR by -> bz

        bl OR bm -> bn

        Args:
            gate (Gate)
        """
        
        for g in self.gates:
<<<<<<< HEAD
            if isinstance(g.input_wires, list):
                if gate.output_wire in g.input_wires:
                    gate.output_gates.append(g)
                    g.input_gates.append(gate)
            else:
                if gate.output_wire == g.input_wires:
                    gate.output_gates.append(g)
                    g.input_gates.append(gate)
=======
            if g.input_wires == gate.output_wire:
                gate.output_gate.append(g)
                g.input_gate = gate
>>>>>>> d99c3b896b530647d86dc9e083a2b65412f633ce


    def create_circuit(self):
        print('Loading gates...')
        for line in self.data:
            line = line.split()
            if line[0] == 'NOT':
                self.gates.append(NOT_Gate(line[1], line[3]))
            elif len(line)== 3:
                self.gates.append(LOAD_Gate(line[0], line[2]))
            else:
                if line[1] == 'AND':
                    self.gates.append(AND_Gate([line[0], line[2]], line[4]))
                elif line[1] == 'OR':
                    self.gates.append(OR_Gate([line[0], line[2]], line[4]))
                elif line[1] == 'LSHIFT':
                    self.gates.append(LSHIFT_Gate([line[0], line[2]], line[4]))
                elif line[1] == 'RSHIFT':
                    self.gates.append(RSHIFT_Gate([line[0], line[2]], line[4]))
        print('Loaded gates.\n')

        print('Connecting gates...')
        for gate in self.gates:
            self.search_gates(gate)
        print('Connected gates.')

    def evaluate(self):
        print('Evaluating...')
        while 'a' not in self.db:
            for g in self.gates:
                if 'a' in self.db:
                    print("\n\n ### FINISHED ###")
                    print(self.db['a'])
                    print("### FINISHED ###\n\n")
                    return
                if not g.evaluated:
                    print(g)
                g.evaluate(self.db)

c = Circuit('input')
c.create_circuit()
c.evaluate()
#print(c.db)


print("")
print("")
print("")

# for g in c.gates:
#     print(g)
#     print("")


# print("DB STATE")
# print(c.db)


