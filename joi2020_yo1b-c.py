n, m = map(int, input().split())
li_a = list(map(int, input().split()))
answer = 0
for a in li_a:
    answer = max(answer, li_a.count(a))
print(answer)
