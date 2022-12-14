with open("2022/13.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i for i in lines if i != '']
lines = list(eval(', '.join(lines)))

start = 0
mid   = 0
end   = 0

for list in lines:
    item = list
    while not type(item) is int and item:
        item = item[0]
    
    
    if item == [] or item < 2:
        start += 1
    elif item >= 2 and item < 6:
        mid += 1
    elif item >= 6:
        end += 1

print((start+1) * (start+mid+2))