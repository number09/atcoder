n = int(input())
num = 0
counter = 0


while counter != n:
    num += 1
    if all(w == str(num)[0] for w in str(num)):
        counter += 1
print(num)
