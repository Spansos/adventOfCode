txt = open('AdventOfCode\\Day7.txt')


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
    for i in range(10):
        line = line.replace(' '+str(i)+' ', '')
    container = line.split('contain')[0]
    containments = line.split('contain')[1].replace(' no other', '').split(',')
    if containments != ['']:
        relations[container] = tuple(containments)

for i in range(len(relations)):
    for j in relations.items():
        for k in j[1]:
            if k in bags:
                bags.add(j[0])
            

print(len(bags)-1)