File = open('AdventOfCode\\Day4.txt', "r").readlines()

currentPassStr = ""
currentPassLs1 = []
currentPassLs2 = []    

num = 0

for i in File:
    if i == "\n":
        currentPassStr = currentPassStr[0:-1]
        currentPassStr = currentPassStr.replace("\n", " ")
        currentPassLs1 = currentPassStr.split(" ")
        
        for i in range(len(currentPassLs1)):
            currentPassLs1[i] = currentPassLs1[i].split(":")

        for i in currentPassLs1:
            currentPassLs2.append(i[0])


        if len(currentPassLs2) == 8 or len(currentPassLs2) == 7 and not "cid" in currentPassLs2:
            num += 1

        currentPassStr = ""
        currentPassLs1 = []
        currentPassLs2 = []

    else:
        currentPassStr += i
    
    
currentPassStr = currentPassStr[0:-1]
currentPassStr = currentPassStr.replace("\n", " ")
currentPassLs1 = currentPassStr.split(" ")

for i in range(len(currentPassLs1)):
    currentPassLs1[i] = currentPassLs1[i].split(":")

for i in currentPassLs1:
    currentPassLs2.append(i[0])

if len(currentPassLs2) == 8 or len(currentPassLs2) == 7 and not "cid" in currentPassLs2:
    num += 1


print(num)