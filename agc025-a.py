n = int(input())

answer = int('9' * 5)
for i in range(1, n):
    str_w = str(n - i)
    str_i = str(i)

    answer = min(
        answer,
        sum([int(w) for w in str_w]) + sum([int(wi) for wi in str_i])
    )
print(answer)

