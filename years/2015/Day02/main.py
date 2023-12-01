with open('Day02/input', 'r') as f:
    data = f.readlines()

slack = 0
ribbon = 0
for box in data:
    dimensions = [int(d) for d in box.split('x')]
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]

    smallest_side = min(l*w,w*h,h*l)
    slack += 2*l*w + 2*w*h + 2*h*l + smallest_side
    
    max_dimension = max(l,w,h)
    min_dimensions = sorted(dimensions)[:2]
    wrap = 2*min_dimensions[0] + 2*min_dimensions[1]
    volume = l*w*h
    ribbon += wrap + volume

print(slack, ribbon)