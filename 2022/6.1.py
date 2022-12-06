with open("2022/6.1", "r") as file:
    code = file.readline()
code = code.strip()

s = set()
i = 4
while len(s) != 4:
    s = set(code[i-4:i])
    i += 1
    
print(i-1)