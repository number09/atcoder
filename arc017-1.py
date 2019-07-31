n = int(input())

for i in range(2, n):
    if n % i == 0:
        print("NO")
        exit(0)
else:
    print("YES")