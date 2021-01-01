import operator
from functools import reduce

n = input()

w_n = list(map(int, n[::-1]))

if len(w_n) > 1:
    ans = (reduce(operator.add, w_n[::2]) - reduce(operator.add, w_n[1::2])) % 11
else:
    ans = sum(w_n) % 11
print(ans)