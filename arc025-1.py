li_d = map(int, input().split())
li_j = map(int, input().split())

print(sum([max(d, j) for d, j in zip(li_d, li_j)]))
