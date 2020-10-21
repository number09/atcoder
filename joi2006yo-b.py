n = int(input())
d_n = {}
for _ in range(n):
    key, val = input().split()
    d_n[key] = val

x = int(input())
li_x = []

for _ in range(x):
    li_x.append(input())

print("".join([d_n.get(x, x) for x in li_x]))
