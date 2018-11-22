a = int(input())
b = int(input())
c = int(input())

li_score = sorted([a, b, c], reverse=True)

for l in [a, b, c]:
    print(li_score.index(l) + 1)
