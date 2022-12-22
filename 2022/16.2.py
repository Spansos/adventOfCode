import functools

with open("2022/16.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
lines = [i.split(' ') for i in lines]
flowrates = {i[1]:int(i[4][5:-1]) for i in lines}
connections = {i[1]:[j.removesuffix(',') for j in i[9:]] for i in lines}


@functools.cache
def max_score(cur, opened, timeleft, elephant):
    if timeleft == 0:
        return max_score('AA', opened, 26, False) if elephant else 0

    if len(opened) == len(flowrates):
        return sum(flowrates.values()) * timeleft
    
    ans = 0
    if flowrates[cur] != 0 and cur not in opened:
        new_opened = frozenset((*opened, cur))
        ans = max(ans, (timeleft-1)*flowrates[cur] + max_score(cur, new_opened, timeleft-1, elephant))
        
    for i in connections[cur]:
        ans = max(ans, max_score(i, opened, timeleft-1, elephant))
    
    return ans


print(max_score('AA', frozenset(), 26, True))