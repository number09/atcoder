n, m = map(int, input().split())

list_k = list()
list_p = list()

for i in range(m):
    list_k.append(list(map(int, input().split())))

list_p = list(map(int, input().split()))

answer = 0

for i in range(2 ** n):
    # print(format(i, 'b').zfill(n))

    switch = format(i, 'b').zfill(n)[::-1]

    for idx, p in enumerate(list_p):
        check_k = list_k[idx][1:]

        target_switch = [switch[k - 1] for k in check_k]

        if target_switch.count('1') % 2 != p:
            break
    else:
        answer += 1

print(answer)
