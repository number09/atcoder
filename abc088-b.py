int_n = int(input())
int_array = list(map(int, input().split()))

int_array.sort(reverse=True)

alice = int_array[::2]

bob = int_array[1::2]

print(sum(alice) - sum(bob))

