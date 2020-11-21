import itertools

n = int(input())
s = input()

for p in itertools.permutations(s, n):
    t = ''.join(p)
    if t != s and t[::-1] != s:
        print(t)
        exit(0)
else:
    print('None')

