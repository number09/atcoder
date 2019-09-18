n = int(input())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
li_c = list(map(int, input().split()))

answer = 0
before = -99

for i in range(n):
    idx = li_a[i]
    answer += li_b[idx - 1]
    if idx == before + 1:
        answer += li_c[idx - 2]
    before = idx
print(answer)


