n, m, c = map(int, input().split())

li_b = list(map(int, input().split()))

codes = list()

for i in range(n):
    codes.append(list(map(int, input().split())))

counter = 0
for code in codes:
    if sum([co * b for co, b in zip(code, li_b)]) + c > 0:
        counter += 1
print(counter)
