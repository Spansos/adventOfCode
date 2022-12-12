import string
from queue import PriorityQueue

with open("2022/12.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]

height_dict = {v:i for i, v in enumerate(string.ascii_lowercase)}
height_dict |= {'S': 0, 'E': 25}

start = ()
end = ()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            char = 'a'
        if char == 'E':
            char = 'z'
            start = (x, y)

def h(node):
    return height_dict[lines[node[1]][node[0]]]

nodes = PriorityQueue()
nodes.put((0, start))

froms = {}

toscores = {}
toscores[start] = 0

finscores = {}
finscores[start] = h(start)

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
dims = (len(lines), len(lines[0]))

while nodes.not_empty:
    cur = nodes.get()
    cur = cur[1]
    
    if lines[cur[1]][cur[0]] == 'a':
        end = cur
        print(cur)
        break
    
    for dir in dirs:
        x, y = cur[0], cur[1]
        nx, ny = x+dir[0], y+dir[1]
        
        if nx >= dims[1] or ny >= dims[0] or nx < 0 or ny < 0:
            continue
        if height_dict[lines[y][x]] > height_dict[lines[ny][nx]] + 1:
            continue
        
        pos_new_score = toscores[cur] + 1
        if pos_new_score < toscores.get((nx, ny), float('inf')):
            toscores[(nx, ny)] = pos_new_score
            froms[(nx, ny)] = cur
            finscores[(nx, ny)] = pos_new_score + h((nx, ny))
            if not (nx, ny) in nodes.queue:
                nodes.put((finscores[(nx, ny)], (nx, ny)))

l = 0
cur = end
while cur := froms.get(cur):
    l += 1
print(l)