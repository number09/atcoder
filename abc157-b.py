li_a = list(input().split())
li_a += list(input().split())
li_a += list(input().split())
n = int(input())

for i in range(n):
    b = input()
    if b in li_a:
        idx = li_a.index(b)
        li_a[idx] = "o"
if any(
    [all(a == "o" for a in li_a[:3]),
    all(a == "o" for a in li_a[3:6]),
    all(a == "o" for a in li_a[6:]),
    all(a == "o" for a in li_a[::3]),
    all(a == "o" for a in li_a[1::3]),
    all(a == "o" for a in li_a[2::3]),
    all(a == "o" for a in li_a[::4]),
    all(a == "o" for a in li_a[2:8:2])]
    ):
    print("Yes")
else:
    print("No")
