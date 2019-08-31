n = int(input())

li_p = list(map(int, input().split()))

if len([x for x, y in zip(li_p, sorted(li_p)) if x != y]) <= 2:
    print("YES")
else:
    print("NO")
