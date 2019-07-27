from itertools import permutations

n, m, l = map(int, input().split())
p, q, r = map(int, input().split())

answer = 0

for tate, yoko, takasa in permutations([n, m, l],3):
    answer = max(answer,(tate // p) * (yoko // q) * (takasa // r))

print(answer)


