n, m = map(int, input().split())

li_m = list()

for _ in range(m):
    li_m.append(int(input()))


if set(li_m).intersection([l + 1 for l in li_m]):
    print(0)
    exit(0)


answer = 1

def pt(length):

    if length == 0:
        return 1

    li_test = [0] * length
    for i in range(length):
        if i == 0:
            li_test[i] = 1
        elif i == 1:
            li_test[i] = li_test[i - 1] + 1
        elif i == len(li_test):
            li_test[i] = li_test[i - 1] + 1
        else:
            li_test[i] = li_test[i - 1] + li_test[i - 2]

    return li_test[-1]


idx_start = 0
idx_end = 0

if len(li_m) != 0:

    for idx, v in enumerate(li_m):
        if idx == 0:
            idx_end = v - 1
        else:
            idx_start = idx_end + 2
            idx_end = v - 1

        subkaidan = idx_end - idx_start

        answer = answer * pt(subkaidan)

        if idx == len(li_m) - 1:
            idx_start = idx_end + 2
            idx_end = n
            subkaidan = idx_end - idx_start

            answer = answer * pt(subkaidan)
else:
    answer = answer * pt(n)


print(answer % 1000000007)
