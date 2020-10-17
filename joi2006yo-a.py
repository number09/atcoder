n = int(input())
li_cards = []
for _ in range(n):
    li_cards.append(list(map(int, input().split())))

score_a = 0
score_b = 0
for c in li_cards:
    if c[0] > c[1]:
        score_a += sum(c)
    elif c[0] < c[1]:
        score_b += sum(c)
    else:
        score_a += c[0]
        score_b += c[1]

print(score_a, score_b)