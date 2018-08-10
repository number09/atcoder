int_n = int(input())
int_k = int(input())

li_x = list(map(int, input().split()))

print(sum([i if i <= abs(i - int_k) else abs(i - int_k) for i in li_x]) * 2)


