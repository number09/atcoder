n = int(input())
li_l = list(map(int, input().split()))

if max(li_l) < sum(li_l) - max(li_l):
    print("Yes")
else:
    print("No")

