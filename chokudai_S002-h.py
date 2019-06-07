
n = int(input())

li_w = list()
for _ in range(n):
    li_w.append(tuple(map(int, input().split())))

for a, b in li_w:
    print(abs(a - b) if a != b else -1)
