abcd = input()

a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])
for X in range(1, 3):
    for Y in range(1, 3):
        for Z in range(1, 3):
            if b * ((-1) ** X) + c * ((-1) ** Y) + d * ((-1) ** Z) == (7 - a):
                op1 = '-' if X == 1 else '+'
                op2 = '-' if Y == 1 else '+'
                op3 = '-' if Z == 1 else '+'
                print("{}{}{}{}{}{}{}=7".format(a, op1, b, op2, c, op3, d))
                exit(0)
