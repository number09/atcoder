from itertools import combinations

li_ant = list()

for _ in range(5):
    li_ant.append(int(input()))

k = int(input())

if all([abs(cmb[0] - cmb[1]) <= k for cmb in combinations(li_ant, 2)]):
    print("Yay!")
else:
    print(":(")
