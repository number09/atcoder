# ひっくりかえされる側からみると、自分より左側に約数？となる数がいくつあるかで
# ひっくり返される数が決まる

# ひっくりかえされる側からみると、自分より左側のコインの並びは無視できる

int_n = int(input())
li_coin = list()
for i in range(int_n):
    li_coin.append(int(input()))

sum = 0.0

for coin in li_coin:
    # coin の約数だけ取り出す
    li_yak = list(filter(lambda x: coin % x == 0, li_coin))
    c_yak = len(li_yak) - 1
    sum += 0.5 if c_yak % 2 != 0 else (c_yak + 2) / (2 * c_yak + 2)


print(sum)
