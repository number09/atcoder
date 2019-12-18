n, m = map(int, input().split())

li_in = list()
for i in range(m):
    li_in.append(list(map(int, input().split())))

w_li_in = sorted(li_in, key=lambda x: x[0], reverse=True)

answer = 0
for item in w_li_in[:-1]:
    if item[0] < n:
        answer += (n - item[0])
print(answer)
