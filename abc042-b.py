int_n, int_l = map(int, input().split())

li_s = list()

for i in range(int_n):
    li_s.append(input())

print("".join(sorted(li_s)))

