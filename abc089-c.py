from itertools import combinations
from collections import defaultdict
n = int(input())

d = defaultdict(int)

for i in range(n):
    d[input()[0]] += 1

w = ['M', 'A', 'R', 'C', 'H']

counter = 0
for w in combinations(w, 3):
    counter += d[w[0]] * d[w[1]] * d[w[2]]

print(counter)
