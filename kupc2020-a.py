n = int(input())
li_addr = []

for _ in range(n):
    li_addr.append(list(map(int, input().split())))

answer = 0
for i in range(n - 1):
    answer += \
        abs(li_addr[i][0] - li_addr[i + 1][0]) + \
        abs(li_addr[i][1] - li_addr[i + 1][1])
print(answer)

