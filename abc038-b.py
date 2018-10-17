
first = list(input().split())
second = list(input().split())

for i in first:
    if any(i == v for v in second):
        print("YES")
        break
else:
    print("NO")


