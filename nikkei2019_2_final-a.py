n = int(input())
li_a = list(map(int, input().split()))

answer = 0
for j in range(1, n - 1):
    l = len([i for i in range(j) if li_a[i] < li_a[j]])
    r = len([k for k in range(j, n) if li_a[j] > li_a[k]])
    answer += l * r
print(answer)
