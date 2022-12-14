with open("2022/13.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i for i in lines if i != '']
lines = eval(', '.join(lines))

def comp(left, right):
    if type(left) is list or type(right) is list:
        left  = [left]  if not type(left)  is list else left
        right = [right] if not type(right) is list else right
    
        for i, j in zip(left, right):
            v =  comp(i, j)
            if v != None:
                return v
    
        if len(left) != len(right):
            return len(left) < len(right)
    else:
        if left != right:
            return left < right


n = 0

for i, (list1, list2) in enumerate(zip(lines[::2], lines[1::2])):
    if comp(list1, list2):
        n += i+1

print(n)