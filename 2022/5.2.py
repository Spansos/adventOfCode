with open("2022/5.1", "r") as file:
    lines = file.readlines()

cargolines = []
movelines  = []
is_move = False
for i in lines:
    if i == '\n':
        is_move = True
        continue
    if is_move:
        movelines.append(i)
    else:
        cargolines.append(i)

cargo = []
for line in reversed(cargolines):
    for x, char in enumerate(line):
        if char.isalpha():
            x = (x-1)//4
            while len(cargo) - 1 < x:
                cargo.append([])
            cargo[x].append(char)

moves = []
for i in movelines:
    i = i.strip()
    words = i.split(' ')
    moves.append((int(words[1]), int(words[3]), int(words[5])))

for move in moves:
    cargo[move[2]-1] += cargo[move[1]-1][-move[0]:]
    for i in range(move[0]):
        cargo[move[1]-1].pop()

print(''.join([i[-1] for i in cargo]))