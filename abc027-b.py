n = int(input())
li_a = list(map(int, input().split()))

bridge = 0

if sum(li_a) % len(li_a) != 0:
    print("-1")
    exit(0)
else:
    ave = sum(li_a) / len(li_a)
    for i in range(len(li_a) - 1):
        if sum(li_a[0:1 + i]) != len(li_a[0:1 + i]) * ave or sum(li_a[1 + i:]) != len(li_a[1 + i:]) * ave:
            bridge += 1

print(bridge)
