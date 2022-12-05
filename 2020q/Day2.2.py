File = open('AdventOfCode\\Day2.txt')
num = 0

for i in File.readlines():
    line = i.replace('-', ' ')
    line = line.replace(': ', ' ')
    line = line.replace("\n", '')
    
    num1, num2, letter, string = line.split(' ')
    
    if string[int(num1)-1] == letter and string[int(num2)-1] != letter or string[int(num2)-1] == letter and string[int(num1)-1] != letter:
        num += 1

print(num)