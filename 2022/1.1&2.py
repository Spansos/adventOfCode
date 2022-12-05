with open("2022/1.1", "r") as file:
    lines = file.readlines()

vals = []

cur_vals = []
for i, v in enumerate(lines):
    if v == '\n':
        vals.append(cur_vals)
        cur_vals = []
    else:
        cur_vals.append(int(v.replace('\n', '')))
cur_vals.append(int(v.replace('\n', '')))

sums = [sum(i) for i in vals]

print(sum(sorted(sums, reverse=True)[:3]))