n = int(input())

li_hi = list()
a = 1
b = 1
for i in range(n):
    li_hi.append(list(map(int, input().split())))

for l in li_hi:
    w = max(a // l[0], b // l[1])
    a = w * l[0]
    b = w * l[1]

print(a + b)


