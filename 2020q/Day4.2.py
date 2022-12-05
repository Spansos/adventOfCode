File = open('AdventOfCode\\Day4.txt')

a = ""
b = []
c = []
num = 0

while True:
    line = File.readline()
    while line != "\n" and line != "":
        a += line
        line = File.readline()
    if line == '':
        b.append(a)
        break
    if line == "\n":
        b.append(a)
        a = ""

popIndexes = []
for i in range(len(b)):
    b[i] = b[i].replace("\n", " ")
    b[i] = b[i].split(" ")
    
    for j in range(len(b[i])):
        if b[i][j] == '' or b[i][j][0:3] == 'cid':
            popIndexes.append((i, j))


popIndexes.reverse()

for i in popIndexes:
    b[i[0]].pop(i[1])



for i in range(len(b)):
    c.append({})
    for j in range(len(b[i])):
        key, value = b[i][j].split(":")
        c[i][key] = value

hcllist = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']



for i in c:
    helpfullist = []
    height = False
    if len(i) == 7:
        #print('a')
        if len(i['byr']) == 4 and int(i['byr']) <= 2002 and int(i['byr']) >= 1920:
            #print('b')
            if len(i['iyr']) == 4 and int(i['iyr']) >= 2010 and int(i['iyr']) <= 2020:
                #print('c')
                if len(i['eyr']) == 4 and int(i['eyr']) >= 2020 and int(i['eyr']) <= 2030:
                    #print('d')
                    if i['hgt'][-2:] == 'cm':
                        if int(i['hgt'][:-2]) >= 150 and int(i['hgt'][:-2]) <= 193:
                            height = True
                    elif i['hgt'][-2:] == 'in':
                        if int(i['hgt'][:2]) >= 59 and int(i['hgt'][:2]) <= 76:
                            height = True
                    if height == True:
                        #print('e')
                        if i['hcl'][0] == "#" and len(i['hcl'][1:]) == 6:
                            for j in i['hcl'][1:]:
                                if j in hcllist:
                                    helpfullist.append(True)
                                else:
                                    helpfullist.append(False)
                            if all(helpfullist):
                                #print('f')
                                if i['pid'].isdecimal() and len(i['pid']) == 9:
                                    #print('g')
                                    if i['ecl'] in ecl:
                                        #print('h')
                                        num +=1

print(num)

                        


