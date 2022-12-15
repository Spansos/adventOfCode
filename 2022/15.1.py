with open("2022/15.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i.split(' ') for i in lines]
sensors = {(int(line[2][2:-1]), (int(line[3][2:-1]))): (int(line[8][2:-1]), int(line[9][2:])) for line in lines}

def is_covered(pos):
    for sens, bcn in sensors.items():
        reach = abs(sens[0]-bcn[0])+abs(sens[1]-bcn[1])
        dist  = abs(sens[0]-pos[0])+abs(sens[1]-pos[1])
        if reach >= dist:
            return True
    return False

minx = float('inf')
maxx = 0
for k, v in sensors.items():
    dist = abs(k[0]-v[0])+abs(k[1]-v[1])
    dy = abs(k[1]-2000000)
    tminx = k[0] - abs(dist-dy)
    tmaxx = k[0] + abs(dist-dy)
    minx = min(minx, tminx-50)
    maxx = max(maxx, tmaxx+50)

n = 0
for i in range(minx, maxx+1):
    if is_covered((i, 2000000)) and not (i, 2000000) in sensors.values():
        n += 1
    # print(i, n)
print(n)