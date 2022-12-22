with open("2022/21", "r") as file:
    lines = file.readlines()
lines = [line.strip().split(':') for line in lines]
monkeys = {line[0]:line[1].strip().split(' ') for line in lines}

def calc(monkey, monkeys):
    command = monkeys[monkey]
    if monkey == 'humn':
        return 'humn'

    if command[0].isnumeric():
        return int(command[0])
    
    val1, val2 = calc(command[0], monkeys), calc(command[2], monkeys)
    if type(val1) is int and type(val2) is int:
        match command[1]:
            case '+':
                return int(val1 + val2)
            case '-':
                return int(val1 - val2)
            case '*':
                return int(val1 * val2)
            case '/':
                return int(val1 / val2)
    else:
        return (val1, command[1], val2)

def calc2(calcs, want):
    if calcs == 'humn':
        return want
    
    known   = calcs[0] if type(calcs[0]) is int else calcs[2]
    unknown = calcs[0] if type(calcs[0]) is tuple or type(calcs[0]) is str else calcs[2]
    match calcs[1]:
        case '+':
            return calc2(unknown, want-known)
        case '*':
            return calc2(unknown, want/known)
        case '-':
            if calcs[0] == known:
                return calc2(unknown, -want+known)
            else:
                return calc2(unknown, want+known)
        case '/':
            if calcs[0] == known:
                return calc2(unknown, known/want)
            else:
                return calc2(unknown, want*known)


val1, val2 = calc(monkeys['root'][0], monkeys), calc(monkeys['root'][2], monkeys)
# print(val1)
# print(val2)
want = val1 if type(val1) is int else val2
new_calcs = val1 if type(val1) is tuple else val2
# print(want)
print(int(calc2(new_calcs, want)))