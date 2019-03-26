n, m = map(int, input().split())

li_shop = list()
for i in range(n):
    li_shop.append(list(map(int, input().split())))

zan = m
money = 0
for shop in sorted(li_shop, key=lambda x: x[0]):
    if zan > shop[1]:
        # すべて買う
        buy = shop[1]
        money += shop[0] * buy
        zan = zan - buy
    else:
        buy = zan
        money += shop[0] * buy
        zan = 0
print(money)
