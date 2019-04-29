n = int(input())
li_v = list(map(int, input().split()))
li_c = list(map(int, input().split()))

li_a = list()

for i in range(n):
    li_a.append(li_v[i] - li_c[i])

print(sum(list(filter(lambda x: x >= 0, li_a))))
