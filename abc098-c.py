int_n = int(input())
str_s = input()

li_west = [0] * int_n
for i in range(int_n - 1):
    if str_s[i] == 'W':
        li_west[i + 1] = li_west[i] + 1
    else:
        li_west[i + 1] = li_west[i]
li_east = [0] * int_n

for i in range(int_n - 1, 0, -1):
    if str_s[i] == 'E':
        li_east[i - 1] = li_east[i] + 1
    else:
        li_east[i - 1] = li_east[i]

minimum = 999999
for i in range(int_n):
    int_w = li_west[i] + li_east[i]
    minimum = min(minimum, int_w)

print(minimum)
