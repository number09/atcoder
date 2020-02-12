n = int(input())
li_a = list(map(int, input().split()))

if len(li_a) == len(set(li_a)):
    print("YES")
else:
    print("NO")
