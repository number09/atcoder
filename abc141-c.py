n, k, q = map(int, input().split())

li_a = list()
d_seikai = dict()
for i in range(q):
    in_a = int(input())
    li_a.append(in_a)
    d_seikai[in_a] = d_seikai.get(in_a, 0) + 1

for m in range(1, n + 1):
    seikai = d_seikai.get(m, 0)
    machigai = q - seikai

    if k <= machigai:
        print("No")
    else:
        print("Yes")

