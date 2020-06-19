n = int(input())
li_a = list(map(int, input().split()))

print(sum([li_a[i+1] - li_a[i] for i in range(len(li_a) - 1)]) / (len(li_a) - 1))
