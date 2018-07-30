int_h, int_w = map(int,input().split())

ar_in = list()
for i in range(int_h):
    ar_in.append(list(input().split()))

print("#" * (int_w + 2))

for i in ar_in:
    print("#" + "".join(i) + "#")

print("#" * (int_w + 2))
