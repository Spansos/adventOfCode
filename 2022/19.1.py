import functools

with open("2022/19.1", "r") as file:
    lines = file.readlines()
lines = [i.strip() for i in lines]
blueprints = [i.split(':')[1].split('.') for i in lines]
blueprints = [[j.split(' ') for j in i] for i in blueprints]
blueprints = [(int(i[0][-2]), int(i[1][-2]), (int(i[2][-5]), int(i[2][-2])), (int(i[3][-5]), int(i[3][-2]))) for i in blueprints]

quality_levels = []
for blueprint in blueprints:
    ore_to_clay     = blueprint[2][0] / blueprint[2][1]
    ore_to_obsidian = blueprint[3][0] / blueprint[3][1]
    
    stuff = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
    bots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    for _ in range(24):
        try:
            cur_ore_to_clay = bots['ore'] / bots['clay']
        except ZeroDivisionError:
            cur_ore_to_clay = float('inf')
            
        try:
            cur_ore_to_obsidian = bots['ore'] / bots['obsidian']
        except ZeroDivisionError:
            cur_ore_to_obsidian = float('inf')
            
        nstuffs = {}
        for bot in bots:
            nstuffs[bot] = bots[bot]
        
        
        # print(ore_to_clay, ore_to_obsidian)
        # print(cur_ore_to_clay, cur_ore_to_obsidian)
        # print(stuff, bots)
        # print()
        if stuff['ore'] >= blueprint[3][0] and stuff['obsidian'] >= blueprint[3][1]:
            stuff['ore'] -= blueprint[3][0]
            stuff['obsidian'] -= blueprint[3][1]
            bots['geode'] += 1
        elif cur_ore_to_obsidian > ore_to_obsidian:
            if stuff['ore'] >= blueprint[2][0] and stuff['clay'] >= blueprint[2][1]:
                stuff['ore'] -= blueprint[2][0]
                stuff['clay'] -= blueprint[2][1]
                bots['obsidian'] += 1
            elif cur_ore_to_clay > ore_to_clay:
                if stuff['ore'] >= blueprint[1]:
                    stuff['ore'] -= blueprint[1]
                    bots['clay'] += 1
            else:
                if stuff['ore'] >= blueprint[0]:
                    stuff['ore'] -= blueprint[0]
                    bots['ore'] += 1
        else:
            if stuff['ore'] >= blueprint[0]:
                stuff['ore'] -= blueprint[0]
                bots['ore'] += 1
        
        for nstuff in nstuffs:
            stuff[nstuff] += nstuffs[nstuff]
    
    print(stuff, bots)