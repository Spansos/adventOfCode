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
while rockc != 2022:
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
            for pos in currock:
                npos = (curx+pos[0], cury+pos[1])
                fallen.add(npos)
                maxy = max(npos[1], maxy)
            break
    
    
    rockc += 1

print(maxy+1)