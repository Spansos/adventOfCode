txt = open('AdventOfCode\\Day7.txt')

num = 0
bags = {'shiny gold'}

relations = {}
for i in txt.readlines():
    line = i
    line = line.replace('\n', '')
    line = line.replace(' bags ', '')
    line = line.replace(' bag ', '')
    line = line.replace(' bags.', '')
    line = line.replace(' bag.', '')
    line = line.replace(' bags', '')
    line = line.replace(' bag', '')
    container = line.split('contain ')[0]
    containments = line.split('contain ')[1].split(', ')
    for j in range(len(containments)):
        containments[j] = tuple(containments[j].split(' ', 1))
    if containments != [''] and containments != [('no', 'other')]:
        relations[container] = tuple(containments)

for i in relations:
    if i == 'shiny gold':
        num += int(relations[i][0][0]) + int(relations[i][1][0])
        print(relations[i], num)