n, k = map(int, input().split())

li_n = list(range(1 , n + 1))
for _ in range(k):
    d = int(input())
    li_a = list(map(int, input().split()))
    for a in li_a:
        if a in li_n:
            li_n.remove(a)
print(len(li_n))
