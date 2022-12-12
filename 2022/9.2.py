import math

with open("2022/9.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]


dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

pos_set = set()

for line in lines:
    dir, times = line.split(' ')
    times = int(times)
    dir = dirs[dir]
    
    for i in range(times):
        rope[0][0] += dir[0]
        rope[0][1] += dir[1]
        
        
        for j in range(1, 10):
            pos1 = rope[j]
            pos2 = rope[j-1]
            dx, dy = pos2[0]-pos1[0], pos2[1]-pos1[1]
            
            if abs(dx) >= 2 and dy == 0:
                pos1[0] += math.copysign(1, dx)
                
            elif abs(dy) >= 2 and dx == 0:
                pos1[1] += math.copysign(1, dy)
                
            elif abs(dy) >= 2 or abs(dx) >= 2:
                pos1[0] += math.copysign(1, dx)
                pos1[1] += math.copysign(1, dy)
            pos_set.add((rope[-1][0], rope[-1][1]))
        # for x in range(6):
        #     for y in range(6):
        #         if [x, y] in rope:
        #             print(rope.index([x, y]), end=' ')
        #         else:
        #             print('.', end=' ')
        #     print()
        # print()

print(len(pos_set))