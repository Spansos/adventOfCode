value_dict = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}

with open("2022/2.1", "r") as file:
    score = 0
    for i in file.readlines():
        a, b = i.strip().split(' ')
        sscore = score

        score += ((value_dict[a]+1)%3 == value_dict[b]%3) * 6
        score += (value_dict[a] == value_dict[b]) * 3
        
        score += value_dict[b]
        print(value_dict[a], value_dict[b], score-sscore)

print(score)