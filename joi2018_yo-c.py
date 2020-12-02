h, w = map(int, input().split())
road = []
for _ in range(h):
    road.append(list(map(int, input().split())))

answer = 1000000000
for a in range(h):
    for b in range(w):
        tmp_answer = 0
        for c in range(h):
            for d in range(w):
                tmp_answer += min(abs(c - a), abs(d - b)) * road[c][d]
        answer = min(answer, tmp_answer)
print(answer)
