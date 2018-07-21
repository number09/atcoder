
int_n = int(input())
ar_int = list(map(int, input().split()))

print(sum([i - 1 for i in ar_int]))


