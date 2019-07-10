from itertools import combinations
import math

counter = 0
n, d = map(int, input().split())

li_n = list()

for i in range(n):
    li_n.append(list(map(int, input().split())))

for con in combinations(li_n, 2):
    result = math.sqrt(sum([(abs(x - y)) ** 2 for x, y in zip(con[0], con[1])]))
    if result.is_integer():
        counter += 1

print(counter)



