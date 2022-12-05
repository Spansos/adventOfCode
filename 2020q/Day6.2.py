txt = open('AdventOfCode\\Day6.txt')
line = txt.readline()
num = 0
alphabeta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while line != '':
    currentGroup = []
    while line != ''  and line != '\n':
        currentGroup.append(line.replace('\n', ''))
        line = txt.readline()
    for i in alphabeta:
        if all(i in letter for letter in currentGroup):
            num += 1
    line = txt.readline()
print(num)