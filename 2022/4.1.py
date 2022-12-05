with open("2022/4.1", "r") as file:
    lines = file.readlines()

duos = [[[int(k) for k in j.split('-')] for j in i.strip().split(',')] for i in lines]

n = 0

for duo in duos:
    if (duo[0][0] >= duo[1][0] and duo[0][1] <= duo[1][1]) or (duo[0][0] <= duo[1][0] and duo[0][1] >= duo[1][1]):
        n += 1

print(n)