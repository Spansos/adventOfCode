rockstr = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""

rocks = []
for i, rock in enumerate(rockstr.split('\n\n')):
    rocks.append(set())
    for y, line in enumerate(rock.split('\n')):
        rocks[i].update({(x, len(rock.split('\n'))-y-1) for x, char in enumerate(line) if char == '#'})

# print(rocks)

with open("2022/17.1", "r") as file:
    jets = file.read()

jetc = 0
rockc = 0
maxy = -1
curx, cury = 0, 0
fallen = set()
adds = []
while rockc != 10000:
    currock = rocks[rockc % 5]
    curx = 2
    cury = maxy + 4
    
    while True:
        # for y in range(20, -1, -1):
        #     for x in range(7):
        #         print('#' if (x, y) in fallen or (x-curx, y-cury) in currock else '.', end='')
        #     print()
        # print(jets[jetc])
        dir = (-1, 1)[jets[jetc] == '>']
        canmove = True
        for pos in currock:
            npos = (curx+pos[0]+dir, cury+pos[1])
            if npos in fallen or npos[0] < 0 or npos[0] > 6:
                canmove = False
                break
        if canmove:
            curx += dir
        jetc += 1
        jetc %= len(jets)
        
        canmove = True
        for pos in currock:
            npos = (curx+pos[0], cury+pos[1]-1)
            if npos in fallen or npos[1] < 0:
                canmove = False
                break
        if canmove:
            cury -= 1
        else:
            nmaxy = maxy
            for pos in currock:
                npos = (curx+pos[0], cury+pos[1])
                fallen.add(npos)
                nmaxy = max(npos[1], nmaxy)
            adds.append(nmaxy - maxy)
            maxy = nmaxy
            break
    
    
    rockc += 1

    

size = 10
while True:
    part = adds[-size:]
    if part == adds[2 * -size: -size]:
        break
    size += 1

start = 0
while True:
    if adds[start:start+size] == part:
        break
    start += 1

cycle = part
front = adds[:start]

print(cycle)
print(front)
print(adds)

blockn = 1000000000000
blockn -= len(front)
cyclen = blockn // len(cycle)
rest = blockn % len(cycle)

print(sum(front) + sum(cycle) * cyclen + sum(cycle[:rest]))
