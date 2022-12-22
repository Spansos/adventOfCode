with open("2022/21", "r") as file:
    lines = file.readlines()
lines = [line.strip().split(':') for line in lines]
monkeys = {line[0]:line[1].strip().split(' ') for line in lines}

def calc(monkey, monkeys):
    command = monkeys[monkey]
    if command[0].isnumeric():
        return int(command[0])
    
    match command[1]:
        case '+':
            return calc(command[0], monkeys) + calc(command[2], monkeys)
        case '-':
            return calc(command[0], monkeys) - calc(command[2], monkeys)
        case '*':
            return calc(command[0], monkeys) * calc(command[2], monkeys)
        case '/':
            return calc(command[0], monkeys) / calc(command[2], monkeys)
    

print(calc('root', monkeys))