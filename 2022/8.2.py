with open("2022/8.1", "r") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

n = 0

for i, v in list(enumerate(lines)):
    for i2, v2 in list(enumerate(v)):
        top = 0
        for j in reversed(lines[:i]):
            top += 1
            if int(j[i2]) >= int(v2):
                break
        bot = 0
        for j in lines[i+1:]:
            bot += 1
            if int(j[i2]) >= int(v2):
                break
        left = 0
        for j in reversed(v[:i2]):
            left += 1
            if int(j) >= int(v2):
                break
        right = 0
        for j in v[i2+1:]:
            right += 1
            if int(j) >= int(v2):
                break
        
        # print(top, bot, left, right)
        
        temp_n = top * bot * left * right
        if temp_n > n:
            n = temp_n

print(n)