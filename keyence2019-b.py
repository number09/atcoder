s = input()

c_word ='keyence'


if c_word in s:
    print("YES")
else:
    for i in range(1, 7):
        w_a = c_word[:i]
        w_b = c_word[i:]

        if s.find(w_a) == 0 and s[len(w_a):][::-1].find(w_b[::-1]) == 0:
            print("YES")
            exit(0)
    else:
        print("NO")



