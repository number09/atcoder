# ひっくりかえされる側からみると、自分より左側に約数？となる数がいくつあるかで
# ひっくり返される数が決まる

# ひっくりかえされる側からみると、自分より左側のコインの並びは無視できる

from itertools import permutations
import math
int_n = int(input())
li_coin = list()
for i in range(int_n):
    li_coin.append(int(input()))

sum = 0
for t in list(permutations(li_coin)):
    for idx in range(len(t)):
        w = list(filter(lambda x: t[idx] % x == 0, t[:idx]))
        # print(t, len(w), t[idx] if len(w) % 2 == 0 else 0)
        sum += 1if len(w) % 2 == 0 else 0


# print(math.factorial(int_n))
print(sum / math.factorial(int_n))
