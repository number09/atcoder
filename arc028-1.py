n, a, b = map(int, input().split())

amari = n % (a + b)
if 1 <= amari <= a:
    print("Ant")
else:
    print("Bug")
