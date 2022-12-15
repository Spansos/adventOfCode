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

fx, fy = 0, 0

x, y = 0, 0
done = False
while y < 4_000_000:
    while x < 4_000_000:
        if not is_covered((x, y)):
            done = True
            fx, fy = x, y
            break
        for sens, bcn in sensors.items():
            rad = abs(sens[0]-bcn[0])+abs(sens[1]-bcn[1])
            dy = abs(sens[1]-y)
            dx = rad-dy
            minx, maxx = sens[0]-dx, sens[0]+dx
            if x >= minx and x <= maxx:
                x = maxx + 1
                break
    # print(y)
    if done:
        break
    y += 1
    if not y%10000:
        print(y/4_000_000)
    x = 0

print(fx*4_000_000 + fy)