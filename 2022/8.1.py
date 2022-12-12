with open("2022/8.1", "r") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

n = len(lines) * len(lines[0])

for i, v in list(enumerate(lines))[1:-1]:
    for i2, v2 in list(enumerate(v))[1:-1]:
        top = [int(j[i2]) for j in lines[:i] if int(j[i2]) >= int(v2)]
        bot = [int(j[i2]) for j in lines[i+1:] if int(j[i2]) >= int(v2)]
        left = [int(j) for j in v[:i2] if int(j) >= int(v2)]
        right = [int(j) for j in v[i2+1:] if int(j) >= int(v2)]
        
        if top and bot and left and right:
            n -= 1

print(n)