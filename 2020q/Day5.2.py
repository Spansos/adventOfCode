txt = open('AdventOfCode\\Day5.txt')

seats = []

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
    
    seats.append((row, column))
    
for i in range(128):
    for j in range(8):
        if not (i, j) in seats:
            print(i, j)

print(81 * 8 + 5)