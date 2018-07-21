ar_int = list(map(int, input().split()))

ar_int.sort()
print(0 + abs(ar_int[1] - ar_int[0]) + abs(ar_int[2] - ar_int[1]))
