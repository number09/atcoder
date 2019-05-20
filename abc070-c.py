from fractions import gcd


n = int(input())
li_t = list()

for _ in range(n):
    li_t.append(int(input()))

# a * b = 最小公倍数 * 最大公約数


def lcm(a, b):
    return (a * b) // gcd(a, b)

work = 1

for t in li_t:
    work = lcm(work, t)

print(work)
