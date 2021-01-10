n = int(input())
li_a = list(map(int,input().split()))
li_a.sort(reverse=True)
sum_n = 0
for i in range(1, n + 1):
    sum_n += (n - 2 * i + 1) * li_a[i-1]
print(sum_n)