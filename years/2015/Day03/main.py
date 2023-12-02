# COMPLETED

with open('Day03/input', 'r') as f:
    data = f.read()

x = 0
santa_x = 0
robo_x = 0

y = 0
santa_y = 0
robo_y = 0

santa = True

positions = []
positions.append((x, y))

for direction in data:
    if santa:
        
        if direction == '^':
            y = santa_y + 1
            x = santa_x
            santa_y += 1
        elif direction == 'v':
            y = santa_y - 1
            x = santa_x
            santa_y -= 1
        elif direction == '>':
            x = santa_x + 1
            y = santa_y
            santa_x += 1
        elif direction == '<':
            x = santa_x - 1
            y = santa_y
            santa_x -= 1
        
    else:
        
        if direction == '^':
            y = robo_y + 1
            x = robo_x
            robo_y += 1
        elif direction == 'v':
            y = robo_y - 1
            x = robo_x
            robo_y -= 1
        elif direction == '>':
            x = robo_x + 1
            y = robo_y
            robo_x += 1
        elif direction == '<':
            x = robo_x - 1
            y = robo_y
            robo_x -= 1
        

    if (x,y) not in positions:
        positions.append((x, y))
    
    santa = not santa

print(len(positions))
