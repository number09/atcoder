int_n = int(input())
arr_int_a = list(map(int, input().split()))
color_val = set([i // 400 for i in arr_int_a if i < 3200])

over = len([i for i in arr_int_a if i >= 3200])

min = len(color_val)
max = min + over if (min + over) <= 8 else 8

print(min,max)



