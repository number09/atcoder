int_n, int_m = map(int, input().split())

li_a = list()
li_b = list()

for i in range(int_n):
    li_a.append(input())

for i in range(int_m):
    li_b.append(input())


for x in range(int_n - int_m + 1):
    for y in range(int_n - int_m + 1):
        li_w = [a[0 + x: int_m + x] for a in li_a[0 + y: int_m + y]]
        if "".join(li_w) == "".join(li_b):
            print("Yes")
            exit(0)
else:
    print("No")
