n, k = map(int, input().split())
li_h = list(map(int, input().split()))

print(len([h for h in li_h if h >= k]))
