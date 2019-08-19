n = int(input())

res = sum(range(1, n + 1))

if res == 1:
    print("BOWWOW")
    exit(0)

for i in range(1, n):
    if i != 1 and res % i == 0:
        print("BOWWOW")
        exit(0)
else:
    print("WANWAN")
