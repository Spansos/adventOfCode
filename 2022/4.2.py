with open("2022/4.1", "r") as file:
    lines = file.readlines()

duos = [[[int(k) for k in j.split('-')] for j in i.strip().split(',')] for i in lines]

n = 0

for duo in duos:
    s1, s2 = set(range(duo[0][0], duo[0][1]+1)), set(range(duo[1][0], duo[1][1]+1))
    if s1.intersection(s2):
        n += 1

print(n)