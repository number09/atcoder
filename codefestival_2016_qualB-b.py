n, a, b = map(int, input().split())
s = input()

count_a = 0
count_b = 0

for w in s:
    if w == "a":
        if (count_a + count_b) < (a + b):
            count_a += 1
            print("Yes")
        else:
            print("No")
    elif w == "b":
        if (count_a + count_b) < (a + b) and count_b < b:
            count_b += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
