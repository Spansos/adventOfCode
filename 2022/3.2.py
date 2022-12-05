import string


with open("2022/3.1", "r") as file:
    lines = file.readlines()

val_dicts = {v:(i+1) for i, v in enumerate(string.ascii_lowercase)}
val_dicts |= {v:(i+27) for i, v in enumerate(string.ascii_uppercase)}

groups = []
group = []
for i in lines:
    group.append(i.strip())
    if len(group) == 3:
        groups.append(group)
        group = []

n = 0
for group in groups:
    s1, s2, s3 = set(group[0]), set(group[1]), set(group[2])
    s1.intersection_update(s2)
    s1.intersection_update(s3)
    n += val_dicts[list(s1)[0]]


print(n)