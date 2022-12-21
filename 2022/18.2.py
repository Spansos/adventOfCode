with open("2022/18.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i.split(',') for i in lines]
coords = [tuple([int(j) for j in i]) for i in lines]
cubes = set(coords)


maxx, maxy, maxz = 0, 0, 0
for i in coords:
    maxx, maxy, maxz = max(maxx, i[0]), max(maxy, i[1]), max(maxz, i[2])
maxx, maxy, maxz = maxx + 1, maxy + 1, maxz + 1
max = maxx, maxy, maxz

done = set()
cando = set(((maxx, maxy, maxz), ))
dirs = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))

while cando:
    cube = cando.pop()
    for i in dirs:
        npos = (cube[0]+i[0], cube[1]+i[1], cube[2]+i[2])
        if npos not in cubes and npos not in done and all([-1 <= i <= j for i, j in zip(npos, max)]):
            cando.add(npos)
    done.add(cube)

for x in range(maxx):
    for y in range(maxy):
        for z in range(maxz):
            if (x, y, z) not in cubes and (x, y, z) not in done:
                cubes.add((x, y, z))



surfaces = set()
for cube in cubes:
    surfcoords = [list(cube) for i in range(6)]
    
    for i in range(3):
        surfcoords[i][i] += .5
    for i in range(3, 6):
        surfcoords[i][i-3] -= .5
        
    surfcoords = [tuple(i) for i in surfcoords]
    
    for i in surfcoords:
        if i in surfaces:
            surfaces.remove(i)
        else:
            surfaces.add(i)

print(len(surfaces))