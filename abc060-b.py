int_a, int_b, int_c = map(int, input().split())

for i in range(1,int_b + 1):
    if int_a * i % int_b == int_c:
        print("YES")
        exit(0)
print("NO")

