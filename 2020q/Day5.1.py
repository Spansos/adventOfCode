txt = open('AdventOfCode\\Day5.txt')

highestId = 0

for i in txt:
    rowRange = range(128)
    for j in i[0:-5]:
        if j == 'F':
            rowRange = rowRange[:len(rowRange)//2]
        else:
            rowRange = rowRange[len(rowRange)//2:]
    
    if i[6] == 'F':
            row = min(rowRange)
    else:
        row = max(rowRange)


    columnRange = range(8)
    for j in i[-4:-1]:
        if j == 'L':
            columnRange = columnRange[:len(columnRange)//2]
        else:
            columnRange = columnRange[len(columnRange)//2:]
    
    if i[7] == 'L':
            column = min(columnRange)
    else:
        column = max(columnRange)
    

    ID = row*8+column
    if ID > highestId:
        highestId = ID

print(highestId)