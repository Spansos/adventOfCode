with open("2022/18.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i.split(',') for i in lines]
coords = [[int(j) for j in i] for i in lines]

surfaces = set()
for coord in coords:
    surfcoords = [coord.copy() for i in range(6)]
    
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