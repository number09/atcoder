n = int(input())
m = int(input())
li_target = list(map(int, input().split()))

li_write = []
for _ in range(m):
    li_write.append(list(map(int, input().split())))

d_answer = {}
for t, write in zip(li_target, li_write):
    wrong_answer = (n - write.count(t))
    for idx, w in enumerate(write):
        if t == w:
            d_answer[idx + 1] = d_answer.get(idx + 1, 0) + 1
            if t == idx + 1:
                d_answer[idx + 1] = d_answer.get(idx + 1, 0) + wrong_answer
for i in range(1, n + 1):
    print(d_answer.get(i, 0))


