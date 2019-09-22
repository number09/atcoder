n = int(input())
li_v = sorted(list(map(int, input().split())))

answer = li_v[0]

for i in range(1, n):
    answer = (answer + li_v[i]) / 2
print(answer)
