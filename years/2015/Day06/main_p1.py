with open('input', 'r') as f:
    data = f.readlines()

class Light():

    def __init__(self, light):
        self.light = light

    def turn(self, mode):
        if mode == "on":
            self.light = True
        else:
            self.light = False

    def toggle(self):
        self.light = not self.light

class Grid():

    def __init__(self, rows, cols):
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Light(False))
            self.grid.append(row)
    
    def count_lights(self):
        count = 0
        for row in self.grid:
            for light in row:
                if light.light:
                    count += 1
        return count

    def turn(self, mode, source, destination):
        for i in range(int(source[0]), int(destination[0])+1):
            for j in range(int(source[1]), int(destination[1])+1):
                self.grid[i][j].turn(mode)

    def toggle(self, source, destination):
        for i in range(int(source[0]), int(destination[0])+1):
            for j in range(int(source[1]), int(destination[1])+1):
                self.grid[i][j].toggle()


grid = Grid(1000, 1000)

i=1
for instruction in data:
    print(f'Processing ({i}/{len(data)}): {instruction}')
    splitted = instruction.split(" ")
    order = splitted[0]
    if order == 'turn':
        mode = splitted[1]
        source = splitted[2].split(',')
        destination = splitted[4].replace("\n", "").split(',')
        grid.turn(mode, source, destination)
    else:
        source = splitted[1].split(',')
        destination = splitted[3].replace("\n", "").split(',')
        grid.toggle(source, destination)
    
    i+=1


count = grid.count_lights()
print(f'Lights on: {count}')