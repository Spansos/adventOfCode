with open("2022/6.1", "r") as file:
    code = file.readline()
code = code.strip()

s = set()
i = 14
while len(s) != 14:
    s = set(code[i-14:i])
    i += 1
    
print(i-1)