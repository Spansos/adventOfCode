with open("2022/7.1") as file:
    lines = file.readlines()

cur_path = []
files = {}

for line in lines:
    line = line.strip()
    if line[:6] == '$ cd /':
        cur_path = []
        continue
    elif line[:7] == '$ cd ..':
        cur_path.pop()
        continue
    elif line[:4] == '$ cd':
        cur_path.append(line[5:])
        continue
    if line[:4] == '$ ls':
        continue
    if line[:3] == 'dir':
        cur_folder = files
        for i in cur_path:
            cur_folder = cur_folder[i]
            
        cur_folder[line.split(' ')[1]] = {}
        continue
    
    cur_folder = files
    for i in cur_path:
        cur_folder = cur_folder[i]
        
    size, name = line.split(' ')
    cur_folder[name] = size


def sum_files(files: dict):
    sum = 0
    for k, v in files.items():
        if type(v) is dict:
            sum += sum_files(v)
        else:
            sum += int(v)
    return sum

size = sum_files(files)
tot_size = size

def do_thing(files: dict):
    global size
    for k, v in files.items():
        if type(v) is dict:
            sum = sum_files(v)
            if sum < size and 70000000 - tot_size + sum > 30000000:
                size = sum
            do_thing(v)

do_thing(files)
print(size)