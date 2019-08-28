n = int(input())

p = ""
for i in range(n):
    p = p + input()

if p.count("R") > p.count("B"):
    print("TAKAHASHI")
elif p.count("R") < p.count("B"):
    print("AOKI")
else:
    print("DRAW")
