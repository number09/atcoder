int_n, int_k = map(int, input().split())

li_x = list(map(int, input().split()))

result = list()
for i in range(int_n - int_k + 1):
    result.append(abs(li_x[i]) + abs(li_x[0 + (int_k - 1) + i] - li_x[0 + i]))

print(min(result))
