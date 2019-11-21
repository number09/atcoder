n = int(input())
li_p = list()
length = 9
answer = 0
for i in range(n):
    w = input()
    li_p.append(w[::-1])
    length = min(length, len(w))

for y in range(length):
    if sum(int(p[y]) for p in li_p) == 0:
        answer += 1
    else:
        break
print(answer)



