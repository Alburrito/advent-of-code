with open('input', 'r') as f:
    data = f.readlines()

class Light():

    def __init__(self, light):
        self.light = light

    def turn(self, mode):
        if mode == "on":
            self.light += 1
        else:
            if self.light > 0:
                self.light -= 1

    def toggle(self):
        self.light += 2

class Grid():

    def __init__(self, rows, cols):
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Light(0))
            self.grid.append(row)
    
    def count_brightness(self):
        brightness = 0
        for row in self.grid:
            for light in row:
                brightness += light.light
        return brightness

    def turn(self, mode, source, destination):
        for i in range(int(source[0]), int(destination[0])+1):
            for j in range(int(source[1]), int(destination[1])+1):
                self.grid[i][j].turn(mode)

    def toggle(self, source, destination):
        for i in range(int(source[0]), int(destination[0])+1):
            for j in range(int(source[1]), int(destination[1])+1):
                self.grid[i][j].toggle()


grid = Grid(1000, 1000)

i=0
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
    i += 1

brightness = grid.count_brightness()
print(f'Lights on: {brightness}')