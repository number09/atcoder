import itertools

d = int(input())
li_d = map(int, input().split())

print(sum(x * y for x, y in itertools.combinations(li_d, 2)))

