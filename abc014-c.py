# いもす法
# https://imoz.jp/algorithms/imos_method.html

r = 1000002

n = int(input())

li_enq = [0] * r

for i in range(n):
    s, e = map(int, input().split())
    li_enq[s] += 1
    li_enq[e + 1] -= 1

for i in range(1, r):
    li_enq[i] += li_enq[i - 1]

print(max(li_enq))


