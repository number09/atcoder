n = int(input())
li_a1 = list(map(int, input().split()))
li_a2 = list(map(int, input().split()))
answer = 0

for i in range(n):
    answer = max(answer, sum(li_a1[:i + 1]) + sum(li_a2[i:]))
print(answer)

