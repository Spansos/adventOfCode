with open("2022/20", "r") as file:
    lines = file.readlines()
lines = [(int(i.strip()), False) for i in lines]

l = len(lines)
i = 0
while i < l:
    if not lines[i][1]:
        print([i[0] for i in lines])
        v = lines.pop(i)[0]
        
        if (i+v)%l:
            lines.insert((i+v)%l, (v, True))
        else:
            lines.append((v, True))
        i = 0
    else:
        i += 1
        
i = lines.index((0, True))
v1, v2, v3 = lines[(i+1000)%l][0], lines[(i+2000)%l][0], lines[(i+3000)%l][0]
print(v1 + v2 + v3)