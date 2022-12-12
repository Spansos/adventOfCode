import math

with open("2022/9.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]


dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

hx = 0
hy = 0
tx = 0
ty = 0

pos_set = set()

for line in lines:
    dir, times = line.split(' ')
    times = int(times)
    dir = dirs[dir]
    
    for i in range(times):
        hx += dir[0]
        hy += dir[1]
        
        dx, dy = hx-tx, hy-ty
        if abs(dx) >= 2 and dy == 0:
            tx += math.copysign(1, dx)
        elif abs(dy) >= 2 and dx == 0:
            ty += math.copysign(1, dy)
        elif abs(dy) >= 2 or abs(dx) >= 2:
            ty += math.copysign(1, dy)
            tx += math.copysign(1, dx)
        pos_set.add((tx, ty))
        
print(len(pos_set))