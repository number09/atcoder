n = int(input())
s = input()
w = n // 2
if s[:w] == s[w:]:
    print("Yes")
else:
    print("No")
