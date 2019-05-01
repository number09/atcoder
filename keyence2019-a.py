n1, n2 , n3, n4 = input().split()

if "".join(sorted([n1, n2, n3, n4])) == "1479":
    print("YES")
else:
    print("NO")
