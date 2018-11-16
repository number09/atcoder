n = int(input())
li_a = list()
for i in range(n):
    li_a.append(int(input()))

result = 0
for i in set(li_a):
    cnt = li_a.count(i)
    if cnt >= 2:
        result += cnt - 1

print(result)