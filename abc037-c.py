n, k = map(int, input().split())
li_input = list(map(int, input().split()))

ruiseki_wa = [0]
for i in range(1, n + 1):
    ruiseki_wa.append(ruiseki_wa[i - 1] + li_input[i - 1])

print(sum((ruiseki_wa[k + i] - ruiseki_wa[i] for i in range(n - k + 1))))


