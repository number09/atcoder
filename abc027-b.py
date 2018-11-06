# WA

n = int(input())
li_a = list(map(int, input().split()))

bridge = 0

if sum(li_a) % len(li_a) != 0:
    print("-1")
    exit(0)
else:
    ave = sum(li_a) / len(li_a)
    for start in range(len(li_a)):
        for end in range(start, len(li_a)):
            w_li = li_a[start:end + 1]
            if sum(w_li) == len(w_li) * ave:
                bridge += len(w_li) - 1
                break

print(bridge)
