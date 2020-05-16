n = int(input())

li_a = list()

for _ in range(n):
    li_a.append(int(input()))

diff = set(range(1, n + 1)) - set(li_a)

if len(diff) > 0:
    w = list(diff)[0]
    d = sum(li_a) + w - sum(range(1, n + 1))
    print(d, w)

else:
    print('Correct')
