import string


with open("2022/3.1", "r") as file:
    lines = file.readlines()

val_dicts = {v:(i+1) for i, v in enumerate(string.ascii_lowercase)}
val_dicts |= {v:(i+27) for i, v in enumerate(string.ascii_uppercase)}

n = 0

lines = [i.strip() for i in lines]
for line in lines:
    c1, c2 = line[:len(line)//2], line[len(line)//2:]

    for i in c1:
        if i in c2:
            n += val_dicts[i]
            break
print(n)