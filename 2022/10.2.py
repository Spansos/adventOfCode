with open("2022/10.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]

def draw(s, c, x):
    sx = (c-1) % 40
    if sx in [x-1, x, x+1]:
        s += '#'
    else:
        s += '.'
    if not (c-1) % 40:
        s += '\n'
    return s

c = 1
x = 1
s = ''
for line in lines:
    if line == 'noop':
        c += 1
        s = draw(s, c, x)
        
    else:
        c += 1
        s = draw(s, c, x)
        c += 1
        x += int(line[5:])
        s = draw(s, c, x)

print(s)