n = int(input())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

li_a_sum = sum(li_a)
answer = 0


for idx in range(n):
    if li_a[idx] >= li_b[idx]:
        li_a[idx] -= li_b[idx]
        li_b[idx] = 0
    else:
        li_b[idx] = li_b[idx] - li_a[idx]
        li_a[idx] = 0

    if li_b[idx] > 0:
        if li_a[idx + 1] >= li_b[idx]:
            li_a[idx + 1] = li_a[idx + 1] - li_b[idx]
            li_b[idx] = 0
        else:
            li_b[idx] -= li_a[idx + 1]
            li_a[idx + 1] = 0

print(li_a_sum - sum(li_a))
