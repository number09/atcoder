li_input = sorted(map(int, input().split()))

if sum(li_input[0:2]) == li_input[2]:
    print("Yes")
else:
    print("No")

