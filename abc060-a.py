str_a, str_b, str_c = input().split()

if str_a[-1] == str_b[0] and str_b[-1] == str_c[0]:
    print("YES")
else:
    print("NO")

