n, m = map(int, input().split())

li_s = list()

for _ in range(n):
    li_s.append(input())

li_a = list()
for _ in range(n):
    li_a.append([0] * m)

for row in range(n):
    for col in range(m):
        target = li_s[row][col]

        if target == '#':
            for r in range(max(row - 1, 0), min(row + 2, n)):
                for c in range(max(col - 1, 0), min(col + 2, m)):
                    li_a[r][c] += 1
for a in li_a:
    print(''.join(str(w) for w in a))

