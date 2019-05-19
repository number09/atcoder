n = int(input())

counter = 0

b_and_a = 0
first_b = 0
last_a = 0
for _ in range(n):
    w = input()
    counter += w.count("AB")

    if w[0] == "B" and w[-1] == "A":
        b_and_a += 1
    elif w[0] == "B":
        first_b += 1
    elif w[-1] == "A":
        last_a += 1
    else:
        pass

if b_and_a == 0:
    counter += min(first_b, last_a)
else:
    if b_and_a >= 2:
        counter += (b_and_a - 1)

    if first_b >= 1:
        counter += 1
        first_b -= 1
    if last_a >= 1:
        counter += 1
        last_a -= 1

    counter += min(first_b, last_a)

print(counter)

