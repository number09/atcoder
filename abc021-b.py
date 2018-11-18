n = int(input())
a, b = map(int, input().split())
k = int(input())
li_p = list(map(int, input().split()))

if a not in li_p and b not in li_p:
    if len(li_p) == len(set(li_p)) and n - 2 >= len(set(li_p)):
        print("YES")
        exit(0)

print("NO")


