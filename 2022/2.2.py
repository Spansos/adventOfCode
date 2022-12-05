move_dict = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
win_dict = {'X':0, 'Y':3, 'Z':6}

with open("2022/2.1", "r") as file:
    score = 0
    for i in file.readlines():
        a, b = i.strip().split(' ')
        sscore = score

        score += win_dict[b]
        if b == 'X':
            score += ((move_dict[a]-2)%3)+1
        elif b == 'Y':
            score += move_dict[a]
        elif b == 'Z':
            score += (move_dict[a]%3)+1
        
        print(move_dict[a], move_dict[b], score-sscore)

print(score)