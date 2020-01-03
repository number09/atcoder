import itertools

n, m = map(int, input().split())

li_a = list()

for i in range(n):
    li_a.append(list(map(int, input().split())))

answer = 0
for x, y in itertools.combinations(range(m), 2):

    sm = 0
    for l in li_a:
        sm += max(l[x], l[y])
    answer = max(answer, sm)
print(answer)

