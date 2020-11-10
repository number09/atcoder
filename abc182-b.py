n = int(input())
li_a = list(map(int, input().split()))


max_k = 0
val = 0
for k in range(2, max(li_a) + 1):
    con = len([a for a in li_a if a % k == 0])
    if val < con:
        max_k = k
        val = con
print(max_k)
