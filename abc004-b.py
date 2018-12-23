li_before = list()

for i in range(4):
    li_before.append(list(input().split()))

for r in range(4):
    print(" ".join([li_before[abs(3 - r)][abs(3 - c)] for c in range(4)]))

