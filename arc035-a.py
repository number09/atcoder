s = input()


for a, b in zip(s, s[::-1]):
    if a != b and (a !="*" and b != "*"):
        print("NO")
        exit(0)
else:
    print("YES")