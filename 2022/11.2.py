with open("2022/11.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]

# one monkey has items: [], operation: lambda, testdiv: int, truemonkey: int, falsemonkey: int
monkeys = []
for i, v in list(enumerate(lines))[::7]:
    items = [int(i.removesuffix(',')) for i in lines[i+1].split(' ')[2:]]
    
    opvals = lines[i+2].split(' ')[-3:]
    if opvals[1] == '+':
        operation = (lambda arg1, arg2: (lambda x: (x if arg1 == 'old' else int(arg1)) + (x if arg2 == 'old' else int(arg2))))(opvals[0], opvals[2])
    elif opvals[1] == '*':
        operation = (lambda arg1, arg2: (lambda x: (x if arg1 == 'old' else int(arg1)) * (x if arg2 == 'old' else int(arg2))))(opvals[0], opvals[2])
        
    testdiv = int(lines[i+3].split(' ')[-1])
    truemon = int(lines[i+4].split(' ')[-1])
    falsemon = int(lines[i+5].split(' ')[-1])
    
    monkeys.append([items, operation, testdiv, truemon, falsemon])

all_divs = [i[2] for i in monkeys]
n = 1
for i in all_divs: n *= i

inspects = [0] * len(monkeys)
for k in range(10000):
    for i, mon in enumerate(monkeys):
        for j, item in enumerate(mon[0]):
            item = mon[1](item)
            item %= n
            # item = item // 3
            
            if not item % mon[2]:
                monkeys[mon[3]][0].append(item)
            else:
                monkeys[mon[4]][0].append(item)
        inspects[i] += len(mon[0])
        mon[0] = []

inspects = sorted(inspects)
print(inspects[-2] * inspects[-1])