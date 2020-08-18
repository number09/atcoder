from itertools import combinations

n = int(input())
li_l = list(map(int, input().split()))

answer = 0
for c in combinations(li_l, 3):
    so = sorted(list(c))

    if (so[0] + so[1]) > so[2] and len(set(so)) == 3:
        answer += 1
print(answer)
