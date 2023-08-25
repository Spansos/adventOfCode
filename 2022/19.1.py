import functools

with open("2022/19.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
blueprints = [i.split(':')[1].split('.') for i in lines]
blueprints = [[j.split(' ') for j in i] for i in blueprints]
blueprints = [(int(i[0][-2]), int(i[1][-2]), (int(i[2][-5]), int(i[2][-2])), (int(i[3][-5]), int(i[3][-2]))) for i in blueprints]

@functools.cache
def calc(blueprint, bots, values):
    