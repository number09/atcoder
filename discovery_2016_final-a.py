n = int(input())
k = [100000,50000,30000,20000,10000]
ans = [0] * n
for i in range(n):
    a = int(input())
    if i < 5:
        ans[a-1] = k[i]
for i in ans:
    print(i)
