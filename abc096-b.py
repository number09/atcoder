int_a, int_b, int_c = list(map(int, input().split()))
int_k = int(input())


ar_order = sorted([int_a, int_b, int_c], reverse=True)

int_max = ar_order.pop(0)

for n in range(int_k):
    int_max *= 2


print(int_max + sum(ar_order))