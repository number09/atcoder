li_input = list(map(int, input().split()))

if li_input.count(7) == 1 and li_input.count(5) == 2:
    print("YES")
else:
    print("NO")
