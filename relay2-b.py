n, q = map(int, input().split())
li_in = []
for _ in range(q):
    li_in.append(list(map(int, input().split())))

for i in li_in:
    a = i[0] - 1
    b = i[1] - 1
    if n == 1:
        print(min(a, b) + 1)
        continue
    while a != b:
        if a > b:
            a = (a - 1) // n
        else:
            b = (b - 1) // n
    print(a + 1)
