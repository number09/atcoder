n, a, b = map(int, input().split())

s_t = set()
for i in range(n):
    s_t.add(int(input()))
answer = 0
for s in s_t:
    if a <= s < b:
        pass
    else:
        answer += 1
print(answer)


