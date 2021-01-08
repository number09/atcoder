n = int(input())

s_men = None
for _ in range(n):
    num = int(input())
    men = set(list(input().split()))

    if s_men is not None:
        s_men = men.intersection(s_men)
    else:
        s_men = men
print(len(s_men))

