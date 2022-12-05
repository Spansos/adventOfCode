txt = open('AdventOfCode\\Day6.txt')
line = txt.readline()
num = 0
while line != '':
    currentGroup = ''
    while line != '' and line != '\n':
        currentGroup += line
        line = txt.readline()
    currentGroup = currentGroup.replace('\n', '')
    currentGroup = set(currentGroup)
    num += len(currentGroup)
    line = txt.readline()
print(num)