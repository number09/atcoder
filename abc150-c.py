import itertools
n = int(input())
t_p = tuple(map(int, input().split()))
t_q = tuple(map(int, input().split()))

l_p = list(itertools.permutations(range(1, n + 1), n))

print(abs((l_p.index(t_p) + 1) - (l_p.index(t_q) + 1)))
