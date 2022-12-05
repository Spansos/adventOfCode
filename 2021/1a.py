with open('1.txt') as f:
    text = f.readlines()

for i, v in enumerate(text):
    text[i] = int(v.replace('\n', ''))

n = 0
for i in range(len(text)-1):
    if text[i] < text[i+1]:
        n += 1

print(n)