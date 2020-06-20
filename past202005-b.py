n, m, q = map(int, input().split())

li_query = list()
for i in range(q):
    li_query.append(input().split())


li_score = [n] * m

member_score = list()

for x in range(n):
    member_score.append(set())

for query in li_query:
    if len(query) == 3:
        li_score[int(query[2]) - 1] -= 1
        member_score[int(query[1]) - 1].add(int(query[2]) - 1)
    else:
        member_idx = int(query[1]) - 1
        ans = 0
        for i in member_score[member_idx]:
            ans += li_score[i]
        print(ans)
