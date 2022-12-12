with open("2022/10.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]

c = 1
x = 1
n = 0
for line in lines:
    if line == 'noop':
        c += 1
        n += x * c if not (c-20) % 40 else 0
    else:
        c += 1
        n += x * c if not (c-20) % 40 else 0
        c += 1
        x += int(line[5:])
        n += x * c if not (c-20) % 40 else 0

print(n)