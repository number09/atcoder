m, n = map(int, input().split())

ans_num = 0
for i in range(m):
    num = list(input().split()).count('1')

    if ans_num < num:
        ans_num = num
print(ans_num)
