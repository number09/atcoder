import itertools
answer = 1000
a1, a2, a3, b1, b2, b3 = map(int, input().split())

for bx in itertools.permutations([b1, b2, b3]):
    answer = min(answer, abs(a1 - bx[0]) + abs(a2 - bx[1]) + abs(a3 - bx[2]))

print(answer)

