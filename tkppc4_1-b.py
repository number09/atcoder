n, k = map(int, input().split())
li_a = list(map(int, input().split()))

li_tmp = list(filter(lambda x: x < k, li_a))
if len(li_tmp) != 0:
    answer = max(li_tmp)
    print(li_a.index(answer) + 1)
else:
    print(-1)


