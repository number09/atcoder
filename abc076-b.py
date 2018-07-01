int_n = int(input())
int_k = int(input())

counter = 1

for i in range(int_n):
    if (counter * 2) <= (counter + int_k):
        counter = counter * 2
    else:
        counter = counter + int_k

print(counter)
