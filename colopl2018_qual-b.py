n, x = map(int, input().split())
s = input()
li_t = list()
for i in range(n):
    li_t.append(int(input()))

answer = 0
for idx, w in enumerate(s):
    if w == '1':
        answer += x if li_t[idx] > x else li_t[idx]
    else:
        answer += li_t[idx]
print(answer)
