File = open('AdventOfCode\\Day2.txt')
num = 0

for i in File.readlines():
    line = i.replace('-', ' ')
    line = line.replace(': ', ' ')
    line = line.replace("\n", '')
    
    low, high, letter, string = line.split(' ')
    
    count = string.count(letter)
    if count >= int(low) and count <= int(high):
        num += 1

print(num)