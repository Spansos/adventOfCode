with open("2022/14.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i.split(' -> ') for i in lines]
lines = [[i.split(',') for i in point] for point in lines]
lines = [[[int(i) for i in point] for point in line] for line in lines]


rockpaths = set()
for line in lines:
    for i, point in enumerate(line[:-1]):
        point1, point2 = point, line[i+1]
        dx, dy = point2[0]-point1[0], point2[1]-point1[1]
        if dx < 0 or dy < 0:
            point1, point2 = point2, point1
            dx, dy = point2[0]-point1[0], point2[1]-point1[1]
            
        if dx:
            for i in range(dx+1):
                rockpaths.add((point1[0]+i, point1[1]))
        else:
            for i in range(dy+1):
                rockpaths.add((point1[0], point1[1]+i))

max_y = max([max([point[1] for point in line]) for line in lines])
sandgen = (500, 0)


cur_sand = [sandgen[0], sandgen[1]]
sands = set()
while cur_sand[1] < max_y:
    down = (cur_sand[0], cur_sand[1]+1)
    down_left = (cur_sand[0]-1, cur_sand[1]+1)
    down_right = (cur_sand[0]+1, cur_sand[1]+1)
    if not down in sands and not down in rockpaths:
        cur_sand[1] += 1
    elif not down_left in sands and not down_left in rockpaths:
        cur_sand[0] -= 1
        cur_sand[1] += 1
    elif not down_right in sands and not down_right in rockpaths:
        cur_sand[0] += 1
        cur_sand[1] += 1
    else:
        sands.add((cur_sand[0], cur_sand[1]))
        cur_sand = [sandgen[0], sandgen[1]]

print(len(sands))