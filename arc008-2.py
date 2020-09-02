import math

n, m = map(int, input().split())
name = input()
kit = input()

kitset = set(kit)


if all([w in kitset for w in set(name)]):
    need_kits = 0
    for x in set(name):
        need = name.count(x)
        exists = kit.count(x)
        need_kits = max(need_kits, math.ceil(need / exists))
    print(need_kits)
else:
    print(-1)

