n = int(input())

li_a = list()

for _ in range(n):
    li_a.append(int(input()))

li_w = [0] * n
li_w[0] = li_a[0]
for i in range(n - 1):
    li_w[i + 1] = li_w[i] + li_a[i + 1]

print(len(list(filter(lambda x: x <= 2018, li_w))))
