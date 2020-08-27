c, d = map(int, input().split())
s = 140
e = 170

answer = 0

work = set()
while True:
    answer += max(0, min(d, e) - max(c, s))
    s = s * 2
    e = e * 2
    if s > d:
        break

print(answer)