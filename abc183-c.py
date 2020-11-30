from itertools import permutations

n, k = map(int, input().split())
li_t = []
answer = 0
for _ in range(n):
    li_t.append(list(map(int, input().split())))

for a in permutations(range(2, n + 1), n - 1):
    li_w = [1] + list(a) + [1]
    tmp = 0
    for s, e in zip(li_w, li_w[1:]):
        tmp += li_t[s - 1][e - 1]
    if tmp == k:
        answer += 1
print(answer)

